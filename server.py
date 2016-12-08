import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='static')

UPLOAD_FOLDER = 'static/music/'
ALLOWED_EXTENSIONS = set(['mp3', 'wave'])

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def homepage():
    return render_template('homepage.html')

# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        file = request.files['audio']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            success_response = {'state': 'SUCCESS'}
            resp = jsonify(**success_response)
            resp.status_code = 200  
            return resp
        else:
            error_response = {'state': 'INVALID', 'error': 'Invalid filetype'}
            resp = jsonify(**error_response)
            resp.status_code = 400
            return resp

if __name__ == '__main__':
    app.run(debug= True)