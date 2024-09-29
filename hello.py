from flask import Flask

app = Flask(__name__)

#Example 2.1
#1. export FLASK_APP=hello.py
#2. flask run
@app.route('/') 
def index():
    return '<h1>Hello World!</h1>'

#Example 2-2. hello.py: Flask application with a dynamic route
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

