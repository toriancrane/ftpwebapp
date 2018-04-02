from flask import(
    Flask,
    flash,
    request,
    redirect,
    url_for,
    render_template,
    make_response,
    jsonify)
from functools import wraps
import random
import string
import requests
import jinja2
import httplib2
import time
import os
import json

app = Flask(__name__)

@app.route('/')
def bucketPage():
    """View contents of bucket"""
    return render_template('bucketcontents.html')

if __name__ == '__main__':
    app.secret_key = 'gDI1tL5OC54UiTF3g18a-bWg'
    app.debug = True
    # app.run(host='0.0.0.0', port=8000)
    app.run(host = '0.0.0.0', port = int(os.environ.get('PORT', 33507)))