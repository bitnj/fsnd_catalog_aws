# Code to establish Flask-WTF forms
from fsnd_item_catalog import images
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SelectField, SubmitField, IntegerField, \
    HiddenField, TextAreaField
from wtforms.validators import DataRequired, Length

# these are needed in order to populate the category choices from the database
from models import Category
from fsnd_item_catalog.database import db_session


# Form for main page
class mainForm(FlaskForm):
    categories = SelectField('Category', coerce=int)

    def __init__(self, *args, **kwargs):
        super(mainForm, self).__init__(*args, **kwargs)
        self.categories.choices = [(category.id, category.name) for category in
                                   db_session.query(Category)]

# Form for adding a new Category


class newCategoryForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Form for editing an existing Category


class editCategoryForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Form for deleting an existing Category


class deleteCategoryForm(FlaskForm):
    submit = SubmitField('Confirm')

# Form for adding a new Item


class newItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    categories = SelectField('Category', coerce=int)
    description = TextAreaField('Description', validators=[DataRequired(),
                                                           Length(max=500)])
    item_image = FileField(
        'Item Image', validators=[
            FileAllowed(
                images, 'Images Only!')])
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(newItemForm, self).__init__(*args, **kwargs)
        self.categories.choices = [(category.id, category.name) for category in
                                   db_session.query(Category)]

# Form for editing an existing Item


class editItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    categories = SelectField('Category', coerce=int)
    description = TextAreaField('Description', validators=[DataRequired(),
                                                           Length(max=500)])
    item_image = FileField(
        'Item Image', validators=[
            DataRequired(), FileAllowed(
                images, 'Images Only!')])
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(editItemForm, self).__init__(*args, **kwargs)
        self.categories.choices = [(category.id, category.name) for category in
                                   db_session.query(Category)]

# Form for deleting an existing item


class deleteItemForm(FlaskForm):
    submit = SubmitField('Confirm')
