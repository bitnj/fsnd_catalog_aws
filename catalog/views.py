from catalog import app

from sqlalchemy import asc
from flask import render_template, request, redirect, flash, url_for, jsonify
from catalog.database import db_session
from models import Users, CatalogItem, Category
from catalog.forms import mainForm, newCategoryForm, newCategoryForm, \
    editCategoryForm, deleteCategoryForm, newItemForm, editItemForm, deleteItemForm
from functools import wraps

# OAuth code separated out for tidyness - import authentication modules
import auth
from auth import getUserInfo

from flask import session as login_session

# for image upload
from catalog import images


# JSON endpoints
@app.route('/categories/JSON')
def showCategoriesJSON():
    categories = db_session.query(Category)
    return jsonify(categories=[c.serialize for c in categories])


@app.route('/categories/<int:category_id>/JSON')
def showCategoryItemsJSON(category_id):
    items = db_session.query(CatalogItem).filter_by(id=category_id)
    return jsonify(items=[i.serialize for i in items])


@app.route('/categories/items/JSON')
def showItemsJSON():
    items = db_session.query(CatalogItem)
    return jsonify(items=[i.serialize for i in items])


@app.route('/categories/items/<int:item_id>/JSON')
def showItemJSON(item_id):
    items = db_session.query(CatalogItem).filter_by(id=item_id).one()
    return jsonify(items.serialize)

# end JSON endpoints


# MAIN VIEW ROUTING
# Decorator for checking login status
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in login_session:
            flash('You must be logged in to access this resource')
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function


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
        items = db_session.query(CatalogItem).filter_by(
            category_id=choice).all()
        return render_template(
            'front.html',
            form=form,
            items=items,
            choice=choice)
    except:
        choice = 0
        items = db_session.query(CatalogItem)
        return render_template(
            'front.html',
            form=form,
            items=items,
            choice=choice)


# create a new category
@app.route('/categories/new/', methods=['GET', 'POST'])
@login_required
def newCategory():
    form = newCategoryForm()
    # validate_on_submit checks that the request is POST and that all validators
    # are True
    if form.validate_on_submit():
        # create a new category record and commit it to the database
        newCategory = Category(name=form.name.data,
                               user_id=login_session['user_id'])
        db_session.add(newCategory)
        db_session.commit()
        flash('New category %s sucessfully added' % newCategory.name)
        return redirect(url_for('showCategories'))
    return render_template('newCategory.html', form=form)


# edit an existing category
@app.route('/categories/edit/<int:category_id>/', methods=['GET', 'POST'])
@login_required
def editCategory(category_id):
    # filter for the passed in category_id
    editedCategory = db_session.query(Category).filter_by(id=category_id).one()
    creator = getUserInfo(editedCategory.user_id)

    if creator.id != login_session['user_id']:
        flash('You must be the owner to edit')
        return redirect(url_for('showCategories'))
    form = editCategoryForm()
    # validate_on_submit checks that the request is POST and that all validators
    # are True
    if form.validate_on_submit():
        editedCategory.name = form.name.data
        db_session.commit()
        flash('Category successfully edited')
        return redirect(url_for('showCategories'))
    return render_template(
        'editCategory.html',
        form=form,
        category=editedCategory)


# delete an existing category
@app.route('/categories/delete/<int:category_id>/', methods=['GET', 'POST'])
@login_required
def deleteCategory(category_id):
    # filter for the passed in category_id
    deletedCategory = db_session.query(
        Category).filter_by(id=category_id).one()
    creator = getUserInfo(deletedCategory.user_id)

    if creator.id != login_session['user_id']:
        flash('You must be the owner to delete')
        return redirect(url_for('showCategories'))
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
    creator = getUserInfo(item.user_id)
    category = db_session.query(Category).filter_by(id=item.category_id).one()
    return render_template('showItem.html', item=item, category=category,
                           creator=creator)


# create a new item
@app.route('/items/item/new/', methods=['GET', 'POST'])
@login_required
def newItem():
    form = newItemForm()
    if request.method == 'POST':
        if form.validate():
            filename = images.save(request.files['item_image'])
            url = images.url(filename)
            # create a new item record and commit it to the database
            newItem = CatalogItem(
                name=form.name.data,
                description=form.description.data,
                category_id=form.categories.data,
                user_id=login_session['user_id'],
                image_filename=filename,
                image_url=url)
            db_session.add(newItem)
            db_session.commit()
            flash('New items %s successfully created' % newItem.name)
            return redirect(url_for('showCategories'))
    return render_template('newItem.html', form=form)


# edit an existing item
@app.route('/items/edit/<int:item_id>/', methods=['GET', 'POST'])
@login_required
def editItem(item_id):
    # filter for the passed in item_id
    editedItem = db_session.query(CatalogItem).filter_by(id=item_id).one()
    creator = getUserInfo(editedItem.user_id)
    
    if creator.id != login_session['user_id']:
        flash('You must be the owner to edit')
        return redirect(url_for('showCategories'))
    form = editItemForm()
    # couldn't seem to set this in the template
    form.categories.data = editedItem.category_id
    form.description.data = editedItem.description
    # validate_on_submit checks that the request is POST and that all validators
    # are True
    if form.validate_on_submit():
        filename = images.save(request.files['item_image'])
        url = images.url(filename)
        editedItem.name = form.name.data
        editedItem.category_id = form.categories.data
        editedItem.description = form.description.data
        editedItem.image_filename = filename
        editedItem.image_url = url
        db_session.commit()
        flash('Item successfully edited')
        return redirect(url_for('showCategories'))
    return render_template('editItem.html', form=form, item=editedItem)


# delete an existing item
@app.route('/items/delete/<int:item_id>/', methods=['GET', 'POST'])
@login_required
def deleteItem(item_id):
    # filter for the passed in item_id
    deletedItem = db_session.query(CatalogItem).filter_by(id=item_id).one()
    creator = getUserInfo(deletedItem.user_id)
    
    if creator.id != login_session['user_id']:
        flash('You must be the owner to delete')
        return redirect(url_for('showCategories'))
    form = deleteItemForm()
    # validate_on_submit checks that the request is POST and that all validators
    # are True
    if form.validate_on_submit():
        db_session.delete(deletedItem)
        db_session.commit()
        flash('Item successfully deleted')
        return redirect(url_for('showCategories'))
    return render_template('deleteItem.html', form=form, item=deletedItem)
