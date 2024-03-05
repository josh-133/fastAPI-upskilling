import os
import sys
import zipfile
import logging
from flask import Flask, render_template, request, send_file, redirect
from werkzeug.utils import secure_filename
from utils import *
from exceltoclass import *

app = Flask(__name__)
UPLOAD_FOLDER = 'storage'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

configuration:bool

configuration = True

@app.route('/')
def index():
    configuration = integrity_check_all(True)
    presets_array = build_presets('array1.xlsx','A2')
    options_array = build_options('array1.xlsx','A1')
    return render_template('index.html', configuration=configuration,presets_array=presets_array, options_array=options_array)

@app.route('/upload_form', methods=['GET'])
def upload_form():
    logging.warning('Navigating to the upload form.')
    return render_template('upload_form.html')

@app.route('/upload', methods=['GET','POST'])
def upload():
    files = request.files.getlist('files')
    for file in files:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        logging.warning('Uploading %s to storage folder.', filename)    
    return redirect('/')

@app.route('/zip_and_download', methods=['GET'])
def zip_and_download():
    # Assuming that you have files in the 'storage' folder
    files_to_zip = os.listdir(app.config['UPLOAD_FOLDER'])
    
    # Create a zip file
    zip_filename = 'zipped_files.zip'
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for filename in files_to_zip:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            zipf.write(file_path, arcname=filename)
            logging.warning('Zipping %s which was in storage folder', filename)
            os.remove(file_path)
            logging.warning('Removing %s from storage folder', filename)
    
    # send the zip file for download
    return send_file(zip_filename, as_attachment=True)

@app.route('/download_and_delete_file')
def download_and_delete_file():
    file_path = '/workspaces/python-flask-exercises/flask/storage/strawberry.jpg'
    
    try:
        response = send_file(file_path, as_attachment=True)
        os.remove(file_path)
        logging.warning('Downloading %s and removing it from the storage folder', file_path)
        return response
    except FileNotFoundError:
        logging.error("ERROR: FILE NOT FOUND 404")
        return "File not found", 404

@app.route('/config')
def config():
    integrity_array = integrity_check_all()
    configuration = integrity_check_all(True)
    return render_template('config.html', configuration=configuration, integrity_array=integrity_array)


if __name__ == '__main__':
    app.run(debug=True,port=5000)
