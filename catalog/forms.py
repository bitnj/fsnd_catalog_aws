# Code to establish Flask-WTF forms
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField, \
HiddenField
from wtforms.validators import DataRequired


# Form for main page
class mainForm(FlaskForm):
    categories = SelectField('category', choices=[])

# Form for adding a new Category
class newCategoryForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('submit')

# Form for editing an existing Category
class editCategoryForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    submit = SubmitField('submit')

# Form for adding a new Item
class newCatalogItem(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
