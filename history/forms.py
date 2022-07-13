from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from wtforms.fields.choices import RadioField, SelectField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from wtforms.widgets.core import SearchInput
from history.models import User, Item
import phonenumbers

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')
    def validate_phone(self, mobileno):
        length=len(str(mobileno.data))
        if(length!=10):
            raise ValidationError('Enter a Valid Phone Number')
    def validate_aadhar(self,aadhar_no):
        l=len(str(aadhar_no.data))
        if(l!=12):
            raise ValidationError('Enter a Valid Aadhar Number')
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    name = StringField(label='Name:', validators=[Length(min=2, max=30), DataRequired()])
    age = IntegerField(label='Age :', validators=[DataRequired()])
    gender = RadioField(label='Gender :',choices=['Male','Female'], validators=[DataRequired()])
    aadhar_no = IntegerField(label="Aadhar Number :",validators=[DataRequired(),validate_aadhar])
    mobileno = StringField(label='Phone :', validators=[DataRequired(),validate_phone])
    address = TextAreaField(label='Address :')
    submit = SubmitField(label='Create Account')
    
    
    
    
class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
    
class UpdateForm(FlaskForm):
    hospital_name = StringField(label = 'Hospital Name :',validators=[DataRequired()])
    doctor_name = StringField(label = 'Doctor Name :',validators=[DataRequired()])
    cause = StringField(label ='Health issue :' ,validators=[DataRequired()])
    city = StringField(label = 'City',validators=[DataRequired()])
    medicines = TextAreaField(label='Medicines :')
    remarks = TextAreaField(label='Remarks :')
    submit = SubmitField(label='Update History')

class DoctorLoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
    
class DoctorView(FlaskForm):
    names=User.query.all()
    search = SelectField(label="Select" ,choices=list(names))
    submit = SubmitField(label= "Search")
    
class AdminLoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
    
class AdminUpdateForm(FlaskForm):
    username=SelectField(label="Username" ,choices=[])
    hospital_name = StringField(label = 'Hospital Name :',validators=[DataRequired()])
    doctor_name = StringField(label = 'Doctor Name :',validators=[DataRequired()])
    cause = StringField(label ='Health issue :' ,validators=[DataRequired()])
    city = StringField(label = 'City',validators=[DataRequired()])
    medicines = TextAreaField(label='Medicines :')
    remarks = TextAreaField(label='Remarks :')
    submit = SubmitField(label='Update History')