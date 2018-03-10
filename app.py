from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = os.path.basename('/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

UPLOAD_COUNT = 0

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_file_extension(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower()


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('photo', None)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join('static', app.config['UPLOAD_FOLDER'], filename))
        print(os.path.join('static', app.config['UPLOAD_FOLDER'], filename))

        return send_file(os.path.join('static', app.config['UPLOAD_FOLDER'], filename), mimetype='image/gif')
    return render_template('error_with_photo.html')

app.run(debug=True)