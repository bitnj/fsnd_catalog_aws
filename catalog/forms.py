# Code to establish Flask-WTF forms
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField, \
HiddenField, TextAreaField
from wtforms.validators import DataRequired

# these are needed in order to populate the category choices from the database
from models import Category
from catalog.database import db_session

# Form for main page
class mainForm(FlaskForm):
    categories = SelectField('Category', coerce=int, 
            choices=[(category.id, category.name)
                for category in db_session.query(Category)])

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
    categories = SelectField('Category', coerce=int, 
            choices=[(category.id, category.name)
                for category in db_session.query(Category)])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Form for editing an existing Item
class editItemForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    categories = SelectField('category', choices=[], validators=[DataRequired()])
    category_id = HiddenField()
    description = StringField('description', validators=[DataRequired()])
    submit = SubmitField('Submit')
