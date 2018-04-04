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
from warrant.exceptions import ForceChangePasswordException
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
folders = my_bucket.meta.client.list_objects(Bucket=my_bucket.name,
                                             Delimiter='/')

auth_client = boto3.client('cognito-idp')
client_id = '5lfps1ae63gbmht8nvem4riccs'
pool_id = 'us-west-2_8HPGr3Zmo'

### S3 User Methods ####
# Find all folders that this user has access to

####  App routes  ####
@app.route('/', methods=['GET', 'POST'])
def homePage():
    if request.method == 'POST':
        #Gather username and password from form
        username = request.form['username']
        password = request.form['password']
        
        #Authenticate user login info
        u = Cognito(pool_id, client_id, username)
        try:
            u.authenticate(password)
            return redirect('/folders')
        except ForceChangePasswordException:
            #new_password = request.form['new_password']
            #u.change_password(password, new_password)
            u.change_password(password, 'Test@12345')
            return redirect('/folders')
            
        #aws = AWSSRP(username=username, password=password, pool_id=pool_id,
        #          client_id=client_id, client=auth_client)
        #tokens = aws.authenticate_user()

        #If user login info authenticated, return buckets page
        #if tokens:
        #    return redirect('/folders')
        #else:
        #    flash('Unable to authenticate user login information.')
        #    return redirect('/')
    else:
        return render_template('index.html')

@app.route('/folders')
def foldersPage():
    """View folders of bucket"""
    return render_template('folders.html', folders=folders)

@app.route('/contents')
def contentsPage():
    """View contents of a folder"""
    objects =  my_bucket.objects.all()
    return render_template('contents.html', objects=objects)
    
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