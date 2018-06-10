from __future__ import print_function
from importlib import import_module
import os
from flask import Flask, render_template, Response, request
from flask_uploads import UploadSet, configure_uploads
import sys
import json
from darkflow.net.build import TFNet
import cv2
from io import BytesIO
import time
from PIL import Image
import numpy as np
from flask_restful import Resource, Api
from werkzeug import secure_filename

options = {
    'model': 'cfg/tiny-yolo-voc-1c.cfg',
    'load': 27625,
    'threshold': 0.1,
}

tfnet = TFNet(options)

app = Flask(__name__)
api=Api(app)

class JSON(Resource):
    def post(self):
        file = request.files['img']
        file_name = "frames/"+file.filename
        file.save(file_name)
        imgcv = cv2.imread(file_name)
        results = tfnet.return_predict(imgcv)
        return str(results)


api.add_resource(JSON, '/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)