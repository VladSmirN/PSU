from app import app
import requests
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', posts=requests.get('https://jsonplaceholder.typicode.com/posts').json())