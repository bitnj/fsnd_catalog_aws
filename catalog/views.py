from catalog import app

from sqlalchemy import asc
from flask import render_template, request, redirect, flash, url_for
from catalog.database import db_session
from models import Users, CatalogItem, Category, Images
from catalog.forms import mainForm, newCategoryForm, newCategoryForm, \
editCategoryForm, deleteCategoryForm, newItemForm, editItemForm, deleteItemForm

# OAuth code separated out for tidyness - import authentication modules
import auth

# list all catalog categories and items for the selected category
@app.route('/', methods=['GET', 'POST'])
@app.route('/categories/', methods=['GET', 'POST'])
def showCategories():
    # create the form and populate the categories from the above query results 
    form = mainForm()

    # if no category is selected then the request will fail so just display all
    # items.  Otherwise display only items for the selected category.
    try:
        choice = request.form['choice']
        items = db_session.query(CatalogItem).filter_by(category_id=choice).all()
        return render_template('front.html', form=form, items=items, choice=choice) 
    except:
        choice = 0
        items = db_session.query(CatalogItem)
        return render_template('front.html', form=form, items=items, choice=choice)


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
        flash('New category %s sucessfully added' % newCategory.name)
        return redirect(url_for('showCategories')) 
    return render_template('newCategory.html', form=form)


# edit an existing category
@app.route('/categories/edit/<int:category_id>/', methods=['GET', 'POST'])
def editCategory(category_id):
    # filter for the passed in category_id
    editedCategory = db_session.query(Category).filter_by(id=category_id).one()
    form = editCategoryForm()
    # validate_on_submit checks that the request is POST and that all validators
    # are True
    if form.validate_on_submit():
        editedCategory.name = form.name.data 
        db_session.commit()
        flash('Category successfully edited')
        return redirect(url_for('showCategories'))
    return render_template('editCategory.html', form=form, category=editedCategory)


# delete an existing category
@app.route('/categories/delete/<int:category_id>/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    # filter for the passed in category_id
    deletedCategory = db_session.query(Category).filter_by(id=category_id).one() 
    form = deleteCategoryForm()
    if form.validate_on_submit(): 
        db_session.delete(deletedCategory)
        db_session.commit()
        flash('Category %s successfully deleted' % deletedCategory.name)
        return redirect(url_for('showCategories'))
    return render_template('deleteCategory.html', form=form,
            category=deletedCategory)


# show an item specific page
@app.route('/categories/item/<int:item_id>/')
def showItem(item_id):
    # filter down to the item_id passed in
    item = db_session.query(CatalogItem).filter_by(id=item_id).one()
    category = db_session.query(Category).filter_by(id=item.category_id).one()
    return render_template('showItem.html', item=item, category=category)
    

# create a new item
@app.route('/items/item/new/', methods=['GET', 'POST'])
def newItem():
    form = newItemForm()
    if request.method == 'POST':
        
        if form.validate():
            # create a new item record and commit it to the database
            newItem = CatalogItem(name=form.name.data,
                    description=form.description.data,
                    category_id=form.categories.data)
            db_session.add(newItem)
            db_session.commit()
            flash('New items %s successfully created' % newItem.name)
            return redirect(url_for('showCategories')) 
    return render_template('newItem.html', form=form)


# edit an existing item 
@app.route('/items/edit/<int:item_id>/', methods=['GET', 'POST'])
def editItem(item_id):
    # filter for the passed in item_id
    editedItem = db_session.query(CatalogItem).filter_by(id=item_id).one()
    form = editItemForm()
    # validate_on_submit checks that the request is POST and that all validators
    # are True
    if form.validate_on_submit():
        editedItem.name = form.name.data 
        editedItem.category_id = form.categories.data
        editedItem.description = form.description.data
        db_session.commit()
        flash('Item successfully edited')
        return redirect(url_for('showCategories'))
    return render_template('editItem.html', form=form, item=editedItem)


# delete an existing item 
@app.route('/items/delete/<int:item_id>/', methods=['GET', 'POST'])
def deleteItem(item_id):
    # filter for the passed in item_id
    deletedItem = db_session.query(CatalogItem).filter_by(id=item_id).one()
    form = deleteItemForm()
    # validate_on_submit checks that the request is POST and that all validators
    # are True
    if form.validate_on_submit():
        db_session.delete(deletedItem)
        db_session.commit()
        flash('Item successfully deleted')
        return redirect(url_for('showCategories'))
    return render_template('deleteItem.html', form=form, item=deletedItem)
