from flask import Flask, request, jsonify
from PIL import Image #python image library
import numpy as np
import requests
from io import BytesIO
import base64
from flask_cors import CORS #comment this on deployment,

app = Flask(__name__)
CORS(app)

@app.route('/colorName', methods=['POST'])
def getColorName():
  raw = request.json.get('image')
  base64_encoded_image = raw.replace("-","/").replace("_","+")
  im = Image.open(BytesIO(base64.b64decode(base64_encoded_image)))

  #extract pixels from the image into a list
  #starting left to right top to bottom
  image_pixels = list(im.getdata())
  data = np.array(im)
  row = len(data)//2
  col = len(data[0])//2

  #get the middle pixel of the m4atrix
  middle_pixel = data[row,col]

  RGB = ",".join([str(value) for value in middle_pixel])
  r,g,b = middle_pixel
  response = requests.get("https://www.thecolorapi.com/id", params = {"rgb": RGB})
  exact = "Exact color: " + response.json()["name"]["value"]

  color_dictionary = {
	  "Black": [0,0,0],
	  "Gray": [127, 127, 127],
	  "Bordeaux": [136, 0, 21],
	  "Red": [237, 28, 36],
	  "Orange": [255, 127, 39],
	  "Salmon": [233, 150, 122],
	  "Brown": [139, 69, 19],
	  "Yellow": [255, 242, 0],
	  "Green": [34, 177, 76],
	  "Blue": [203, 228, 253],
	  "Dark blue": [0, 162, 232],
	  "Purple": [63, 72, 204],
	  "White": [255, 255, 255],
	  "Light gray": [195, 195, 195],
	  "Light brown": [185, 122, 87],
	  "Light pink": [255, 174, 201],
	  "Dark yellow": [255, 201, 14],
	  "Light yellow": [239, 228, 176],
	  "Light green": [181, 230, 29],
	  "Light blue": [153, 217, 234],
	  "Dark blue": [112, 146, 190],
	  "Light purple": [200, 191, 231],
	}

  colors = np.array(list(color_dictionary.values())) # [[0,0,0], [127,127,...],...]
	# returns 1 list  --> the distance from the pixel to all the colors [distance from our pixel to black, distance from our pixel to gray, ...]
  distances = np.sqrt(np.sum((colors-middle_pixel)**2,axis=1)) 
  index_of_smallest = np.where(distances==np.amin(distances)) # then we just take the min of that array 
  smallest_distance = index_of_smallest[0][0]
	
  message = "First closest color: "
  next_closest = message + str(list(color_dictionary.keys())[smallest_distance])

  return [exact, next_closest]

if __name__ == '__main__':
  app.run()