from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password1')])
    is_company = BooleanField('Is Company', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me', validators=[DataRequired()])
    submit = SubmitField('Login')


class JobSeekerForm(FlaskForm):
    user_id = IntegerField('User Id', validators=[DataRequired()])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = IntegerField('Phone', validators=[DataRequired()])
    address = TextAreaField('Address', validators=[DataRequired()])
    programming_languages = StringField('Programming Languages', validators=[DataRequired()])
    tools = StringField('Tools', validators=[DataRequired()])
    degree = StringField('Degree', validators=[DataRequired()])
    dept = StringField('Department', validators=[DataRequired()])
    current_status = StringField('Current Status', validators=[DataRequired()])
    cgpa = IntegerField('CGPA', validators=[DataRequired()])
    x_percent = IntegerField('X Percent', validators=[DataRequired()])
    xii_percent = IntegerField('XII Percent', validators=[DataRequired()])
    submit = SubmitField('Submit')


class CompanyForm(FlaskForm):
    user_id = IntegerField('User Id', validators=[DataRequired()])
    com_name = StringField('Company Name', validators=[DataRequired()])
    com_address = TextAreaField('Company Address', validators=[DataRequired()])
    submit = SubmitField('Submit')


class JobOfferForm(FlaskForm):
    company_id = IntegerField('Company Id', validators=[DataRequired()])
    job_title = StringField('Job Title', validators=[DataRequired()])
    total_applications = IntegerField('Total Applications', validators=[DataRequired()])
    skill_required = StringField('Skill Required', validators=[DataRequired()])


class JobRequestForm(FlaskForm):
    job_offer = IntegerField('Job Offer Id', validators=[DataRequired()])
    job_seeker = IntegerField('Job Seeker Id', validators=[DataRequired()])
