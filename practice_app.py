import flask
from flask import Flask
app=Flask(__name__)
@app.route('/')
def home_function():
    return " I am in the home page"
@app.route('/new_page')
def new_page_function():
    return "I am in a new page"