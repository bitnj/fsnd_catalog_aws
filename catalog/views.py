from catalog import app

from sqlalchemy import asc
from flask import render_template, request, redirect, flash, url_for
from catalog.database import db_session
from models import Users, CatalogItem, Category, Images
from catalog.forms import mainForm, newCategoryForm, newCategoryForm, \
editCategoryForm


# beginning of all app routing

# list all catalog categories and items for the selected category
@app.route('/', methods=['GET', 'POST'])
@app.route('/categories/', methods=['GET', 'POST'])
def showCategories():
    # get all top-level categories
    categories = db_session.query(Category).order_by(asc(Category.name))
    # create the form and populate the categories from the above query results 
    form = mainForm()
    form.categories.choices = [(category.id, category.name) for category in categories]

    # if no category is selected then the request will fail so just display all
    # items.  Otherwise display only items for the selected category.
    try:    
        choice = request.form['choice']
        items = db_session.query(CatalogItem).filter_by(category_id=choice).all()
        return render_template('front.html', form=form, items=items,
            choice=choice) 
    except:
        choice = 0
        items = db_session.query(CatalogItem)
        return render_template('front.html', form=form, items=items,
                choice=choice)


# create a new category
@app.route('/categories/new/', methods=['GET', 'POST'])
def newCategory():
    form = newCategoryForm()
    # validate_on_submit checks that the request is POST and that all validators
    # are True
    if form.validate_on_submit():
        # create a new category record and commit it to the database
        newCategory = Category(name=form.name.data)
        db_session.add(newCategory)
        db_session.commit()
        return redirect('/categories/') 
    return render_template('newCategory.html', form=form)


# edit an existing category
@app.route('/categories/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    # filter for the passed in category_id
    editedCategory = db_session.query(Category).filter_by(id=category_id).one()
    form = editCategoryForm()
    # validate_on_submit checks that the request is POST and that all validators
    # are True
    if form.validate_on_submit():
        editedCategory.name = form.name.data 
        db_session.commit() 
        return redirect(url_for('showCategories'))
    return render_template('editCategory.html', form=form, category=editedCategory)


# delete an existing category
@app.route('/categories/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    # filter for the passed in category_id
    db_session.query(Category).filter_by(id=category_id).delete()
    db_session.commit()
    return redirect(url_for('showCategories'))
