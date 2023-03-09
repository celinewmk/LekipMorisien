from PIL import Image #python image library
import numpy as np
import requests
from io import BytesIO
import base64
import json

def lambda_handler(event, context):
  print(event)
  base64_encoded_image = event["image"]
  try:
    middle_pixel = get_middle_pixel_RGB(base64_encoded_image)
    print(middle_pixel)
    colors = {
        "exact": get_exact_color(middle_pixel),
        "next_closest": get_closest_color(middle_pixel),
    }
    print(colors)
  except Exception as e:
    exception_type = e.__class__.__name__
    exception_message = str(e)
    exception_obj = {
        "isError": True,
        "type": exception_type,
        "message": exception_message
    }
    raise Exception(exception_obj)
  
  headers = {
      "Access-Control-Allow-Headers": "Content-Type",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "OPTIONS,POST",
  }
  return {
      "statusCode": 200,
      "headers": json.dumps(headers),
      "body": json.dumps(colors),
  }
  
#######################
  
def get_middle_pixel_RGB(base64_encoded_image):
  try:
    im = Image.open(BytesIO(base64.b64decode(base64_encoded_image))).convert("RGB")
  except Exception as e:
    print("Error Reading File")
    raise e

  # extract pixels from the image into a list
  # starting left to right top to bottom
  image_pixels = list(im.getdata())
  data = np.array(im)
  row = len(data) // 2
  col = len(data[0]) // 2

  # get the middle pixel of the matrix
  return data[row, col]

def get_closest_color(middle_pixel):
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
	  "Sky blue": [203, 228, 253],
	  "Dark blue": [0, 162, 232],
    "Navy blue": [12, 7, 93],
	  "Blue": [63, 72, 204],
	  "White": [255, 255, 255],
	  "Light gray": [195, 195, 195],
	  "Light brown": [185, 122, 87],
	  "Light pink": [255, 174, 201],
	  "Dark yellow": [255, 201, 14],
	  "Light yellow": [255, 255, 102],
	  "Light green": [181, 230, 29],
    "Dark green": [0, 100, 0],
	  "Turquoise blue": [153, 217, 234],
	  "Dark blue": [112, 146, 190],
	  "Light purple": [200, 191, 231],
	}

  colors = np.array(list(color_dictionary.values())) # [[0,0,0], [127,127,...],...]
	# returns 1 list  --> the distance from the pixel to all the colors [distance from our pixel to black, distance from our pixel to gray, ...]
  distances = np.sqrt(np.sum((colors-middle_pixel)**2,axis=1)) 
  index_of_smallest = np.where(distances==np.amin(distances)) # then we just take the min of that array 
  smallest_distance = index_of_smallest[0][0]
  
  return str(list(color_dictionary.keys())[smallest_distance])
    
def get_exact_color(middle_pixel):
  try:
    RGB = ",".join([str(value) for value in middle_pixel])
    response = requests.get("https://www.thecolorapi.com/id", params = {"rgb": RGB})
  except Exception as e:
    print("Error Getting Exact Color")
    return e

  return response.json()["name"]["value"]