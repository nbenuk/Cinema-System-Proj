from flask_wtf import FlaskForm
from flask import request
from wtforms import TextField, SubmitField, TextAreaField, PasswordField, StringField, SelectMultipleField
from wtforms.validators import DataRequired, Required, Email, EqualTo, ValidationError, Length
from .models import Member, Guest, Admin, Movies, Screening, Booking, Payment


class SignUpForm(FlaskForm):

    username = StringField('Username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(),Email()])
    user_phone = IntegerField('Phone Number', validators = [DataRequired()])
    user_age = IntegerField('Age', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    repeatPassword = PasswordField('repeat password', validators=[DataRequired(), EqualTo('password')])
    register = SubmitField('Register')

    def validate_username(self, username):
        user = Member.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('This username already exists. Please choose a different username.')

    def validate_email(self, email):
        user = Member.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('This email address already exists. Please use a different email address')


class LoginForm(FlaskForm):
    username = TextField('username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(),Email()])
    password = PasswordField('password', validators = [DataRequired()])
    #signin = SubmitField('Sign In')

class AdminLoginForm(FlaskForm):
    username = TextField('username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(),Email()])
    password = PasswordField('password', validators = [DataRequired()])

class MoviesForm(FlaskForm):
    movie_name = TextField('Movie Name', validators = [DataRequired()])
    movie_genre = TextField('Movie Genre', validators = [DataRequired()])
    movie_age_rate = TextField('Movie Age Rate', validators = [DataRequired()])
    movie_release_date = DateField('Release Date', format='%Y-%m-%d')
    Movie_end_date = DateField('End Date', format='%Y-%m-%d')

    def validate_enddate_field(form, field):
        if field.data < form.startdate_field.data:
            raise ValidationError("End date must not be earlier than start date.")

class BookingForm(FlaskForm):
    #movie_name = SelectMultipleField('Movie Name', choices=[('example movie')])
    movie_name = TextField('Movie Name', validators = [DataRequired()])
    #movie_date = SelectMultipleField('Movie Date', choices=[('example dates')])
    movie_date = DateField('Release Date', format='%Y-%m-%d')
    #screen_time = SelectMultipleField('Screen Time', choices=[('example times')])
    screen_time = TextField('Screen Time', validators = [DataRequired()])
    seatings = SelectMultipleField('Movie Seating', choices=[('premium'), ('classic')])
    #num_of_tickets = SelectMultipleField('Tickets', choices=[('1'), ('2'), ...])
    tickets = TextField('Tickets', validators = [DataRequired()])

class PaymentForm(FlaskForm):
    card_type = SelectMultipleField('Card Type', choices=[('MasterCard'), ('Visa')])
    card_num = TextField('Card Number', validators=[DataRequired()])
    card_sec_code = PasswordField('Security Number', validators=[DataRequired()])

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    r_password = PasswordField(
        'Repeat Password', validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField('Request Password Reset')
