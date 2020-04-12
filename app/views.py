from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/interviews')
def interviews():
    return render_template('interviews.html')
