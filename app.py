from flask import(
    Flask,
    flash,
    request,
    redirect,
    url_for,
    render_template,
    make_response,
    jsonify)
from warrant import Cognito
from warrant.aws_srp import AWSSRP
import boto3
import string
import requests
import jinja2
import httplib2
import os

app = Flask(__name__)

#####     Global Resources    ####
s3 = boto3.resource('s3')
my_bucket = s3.Bucket('mb3-demo-files')

auth_client = boto3.client('cognito-idp')

####  App routes  ####
@app.route('/')
def homePage():
    #if request.method == 'POST':
        #Gather username and password from form
    #   username = request.form['username]'
    #   password = request.form['password']
    
    #   aws = AWSSRP(username=username, password=password, pool_id='us-west-2_cu4oyzS4u',
    #               client_id='33gmire0kn5u3eg7m3ah736qsk', client_secret='i2srq6b23s4sfkh89u6kb1e1oo7mefsrinv0deb345vsqiq6d8e',
    #               client=auth_client)
    #   tokens = aws.authenticate_user()
    #   if tokens:
    #       return render_template('buckets.html')
    
    return render_template('buckets.html')

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