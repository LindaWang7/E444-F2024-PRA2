# from flask import Flask, render_template, session, redirect, url_for, flash
# from flask_bootstrap import Bootstrap
# from flask_moment import Moment
# import datetime
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired, Email, Regexp

# app = Flask(__name__)
# bootstrap = Bootstrap(app)
# moment = Moment(app)
# app.config['SECRET_KEY'] = 'hard to guess string'

# # TO RUN
# #1. export FLASK_APP=hello.py
# #2. flask run


# #======Example 2.1 & 2.2=========
# """
# @app.route('/') 
# def index():
#     return '<h1>Hello World!</h1>'
# #Example 2-2. hello.py: Flask application with a dynamic route
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, {}!</h1>'.format(name)
# """


# #======Activity 1.3=========
# """
# @app.route('/')
# def index():
#     date = datetime.datetime.now(datetime.timezone.utc)
#     return render_template("user.html", current_time=date)

# @app.route('/user/<name>')
# def user(name):
#  return render_template('user.html', name=name)

# @app.errorhandler(404)
# def page_not_found(e):
#  return render_template('404.html'), 404
# @app.errorhandler(500)
# def internal_server_error(e):
#  return render_template('500.html'), 500

# if __name__ == '__main__':
#     app.run(debug=True)

#     """


# #======Activity 1.4=========


# class NameForm(FlaskForm):
#     name = StringField('What is your name?', validators=[DataRequired()])
#     email = StringField("What is your UofT email?", validators=[Email(), Regexp(".+utoronto.ca$")])
#     submit = SubmitField('Submit')

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = NameForm()

#     # Get the current time in UTC and pass it to the template
#     current_time = datetime.datetime.utcnow()  # Fix this call

#     # Store old values (if any)
#     old_name = session.get('name')
#     old_email = session.get('email')

#     if form.validate_on_submit():
#         name = form.name.data
#         email = form.email.data
        
#         # Check if the name or email has changed, and flash appropriate messages
#         if old_name and old_name != name:
#             flash('Looks like you have changed your name!', 'warning')
#         if old_email and old_email != email:
#             flash('Looks like you have changed your email!', 'warning')

#         # Valid UofT email check
#         if 'utoronto' in email:
#             flash('Welcome UofT student!', 'success')
#         else:
#             flash('Please use a valid UofT email address.', 'danger')
#             email = None  # Invalid email is not stored

#         # Save new data to session
#         session['name'] = name
#         session['email'] = email

#         return redirect(url_for('index'))

#     return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'), current_time=current_time)


# @app.route('/user/<name>')
# def user(name):
#  return render_template('user.html', name=name)

# @app.errorhandler(404)
# def page_not_found(e):
#  return render_template('404.html'), 404
# @app.errorhandler(500)
# def internal_server_error(e):
#  return render_template('500.html'), 500

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY']= 'SECRET_KEY_SECRET_KEY'

from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email

class NameEmailForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('What is your UofT Email Address?', validators=[DataRequired()]) # no need Email()?
    submit = SubmitField('Submit')


@app.route('/',methods=['GET','POST'])
def index():
    form = NameEmailForm()
    if form.validate_on_submit():
        old_name, old_email = session.get('name'), session.get('email')
        # check for flash message
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')

        session['name']= form.name.data
        session['email']= form.email.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), 
                           email=session.get('email'), current_time=datetime.utcnow())
