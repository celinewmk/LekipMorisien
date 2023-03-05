from flask import Flask, request, jsonify
from PIL import Image #python image library
import numpy as np
import requests
from io import BytesIO
import base64
from flask_cors import CORS #comment this on deployment,

app = Flask(__name__)
CORS(app)

@app.route('/colorName')
def getColorName():
  raw = request.args.get("image")
  base64_encoded_image = raw.replace("-","/").replace("_","+")
  im = Image.open(BytesIO(base64.b64decode(base64_encoded_image)))

  #extract pixels from the image into a list
  #starting left to right top to bottom
  image_pixels = list(im.getdata())
  data = np.array(im)
  row = len(data)//2
  col = len(data[0])//2

  #get the middle pixel of the matrix
  middle_pixel = data[row,col]

  RGB = ",".join([str(value) for value in middle_pixel])
  r,g,b = middle_pixel
  response = requests.get("https://www.thecolorapi.com/id", params = {"rgb": RGB})
  return (response.json()["name"]["value"])

