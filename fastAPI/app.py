import os
import zipfile
import logging
# from flask import Flask, render_template, request, send_file, redirect
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from utils import *
from exceltoclass import *

app = FastAPI()

app.mount("/templates", StaticFiles(directory="templates"), name="templates")

UPLOAD_FOLDER = 'storage'
configuration = True

@app.get('/')
async def index():
    global configuration
    configuration = integrity_check_all(True)
    presets_array = build_presets('array1.xlsx','A2')
    options_array = build_options('array1.xlsx','A1')
    return FileResponse('./templates/index.html')

@app.get('/upload_form')
async def upload_form():
    logging.warning('Navigating to the upload form.')
    return FileResponse('./templates/upload_form.html')

@app.post('/upload')
async def upload(files: List[UploadFile] = File('files')):
    for file in files:
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(filename, "wb") as buffer:
            buffer.write(await file.read())
        logging.warning('Uploading %s to storage folder.', filename)    
    return RedirectResponse(url="/", status_code=303)

@app.get('/zip_and_download')
async def zip_and_download():
    # Assuming that you have files in the 'storage' folder
    files_to_zip = os.listdir(UPLOAD_FOLDER)
    
    # Create a zip file
    zip_filename = 'zipped_files.zip'
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for filename in files_to_zip:
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            zipf.write(file_path, arcname=filename)
            logging.warning('Zipping %s which was in storage folder', filename)
            os.remove(file_path)
            logging.warning('Removing %s from storage folder', filename)
    
    # send the zip file for download
    return FileResponse(zip_filename, media_type='application/zip', filename=zip_filename)

@app.get('/download_and_delete_file')
def download_and_delete_file():
    file_name = 'strawberry.jpg'
    file_path = os.path.join(UPLOAD_FOLDER, file_name)
    if not os.path.exists(file_path):
        logging.error("ERROR: FILE NOT FOUND 404")
        raise HTTPException(status_code=404, detail="File not found")
    
    try:
        response = FileResponse(path=file_path, media_type='image/jpg', filename=file_name)
        logging.warning('Downloading %s', file_name)
        return response
    except FileNotFoundError:
        logging.error("ERROR: FILE NOT FOUND 404")
        raise HTTPException(status_code=404, detail="File not found")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
            logging.warning('Removing %s from the storage folder', file_name)

@app.get('/config')
async def config():
    integrity_array = integrity_check_all()
    configuration = integrity_check_all(True)
    return {
        "configuration": configuration, 
        "integrity_array": integrity_array,
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
