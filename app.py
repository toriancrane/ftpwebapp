from flask import(
    Flask,
    flash,
    request,
    redirect,
    url_for,
    render_template,
    make_response,
    jsonify)
import boto3
import string
import requests
import jinja2
import httplib2
import os

app = Flask(__name__)

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('mb3-demo-files')

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/objects')
def bucketPage():
    """View contents of bucket"""
    objects =  my_bucket.objects.all()
    return render_template('bucketcontents.html', objects=objects)

@app.route('/upload')
def uploadPage():
    """Upload new items to bucket"""
    #if request.method == 'POST':
    #else:
    return render_template('uploadobject.html')

if __name__ == '__main__':
    app.secret_key = 'gDI1tL5OC54UiTF3g18a-bWg'
    app.debug = True
    # app.run(host='0.0.0.0', port=8000)
    app.run(host = '0.0.0.0', port = int(os.environ.get('PORT', 33507)))