import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from server.utility import analyzer, mp3_converter
from server.redis.client import RedisQueue
from server.worker.queue_subscribe import QueueSubscribeWorker
import redis
import json

app = Flask(__name__, static_folder='static')

UPLOAD_FOLDER = 'static/music/'
ALLOWED_EXTENSIONS = set(['mp3', 'wave'])

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

redis_client = redis.StrictRedis("localhost")
redis_queue = RedisQueue('client_publisher', 'song_queue', redis_client)

queue_subscribe_worker = QueueSubscribeWorker('worker 1', redis_queue)
queue_subscribe_worker.daemon = True
queue_subscribe_worker.start()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/api/songs', methods=['GET', 'DELETE'])
def song_list():
    if request.method == 'GET':
        redis_messages = redis_queue.get_list()

        song_list = []
        if redis_messages is not None:
            song_list = [ json.loads(a)['data']['filename'] for a in redis_messages ]

        return jsonify(song_list)

    elif request.method == 'DELETE':
        redis_queue.delete()

        success_message = {'state': 'SUCCESS'}
        return jsonify(**success_message)


# Route that will process the file upload
@app.route('/api/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        file = request.files['audio']
        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)
            full_filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(full_filepath)

            # Convert to WAV file
            full_wavfilepath = mp3_converter.convert_mp3_to_wav(full_filepath)

            # Publish to redis queue
            data = {
                'filepath': full_wavfilepath,
                'filename': filename
            }
            redis_queue.queue(data)

            success_response = {'state': 'SUCCESS'}
            resp = jsonify(**success_response)
            resp.status_code = 200  
            return resp

        else:
            error_response = {'state': 'INVALID', 'error': 'Invalid filetype'}
            resp = jsonify(**error_response)
            resp.status_code = 400
            return resp
    else:
        error_response = {'state': 'INVALID', 'error': 'Invalid filetype'}
        resp = jsonify(**error_response)
        resp.status_code = 400
        return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug= True)