from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

# TO RUN
#1. export FLASK_APP=hello.py
#2. flask run


#======Example 2.1 & 2.2=========
# @app.route('/') 
# def index():
#     return '<h1>Hello World!</h1>'
# #Example 2-2. hello.py: Flask application with a dynamic route
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, {}!</h1>'.format(name)


#======Activity 1.3=========
@app.route('/')
def index():
 return render_template('index.html')
@app.route('/user/<name>')
def user(name):
 return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500