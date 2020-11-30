from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class Facility_Info(FlaskForm):
    category = StringField('category', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    time = StringField('time', validators=[DataRequired()])
    home_url = StringField('home_url', validators=[DataRequired()])
    menu_url = StringField('menu_url', validators=[DataRequired()])
    reserv_url = StringField('reserv_url', validators=[DataRequired()])
    phone_num = StringField('phone_num', validators=[DataRequired()])
    submit = SubmitField('Add')