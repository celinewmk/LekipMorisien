#function that accepts one pixel from the middle of an image and outputs its color


# TODO this will be read from an image we take instead of reading locally
# import image
from PIL import Image #python image library
import numpy as np
import requests

#create image obj and open for reading

im = Image.open("C:\\Users\\selin\\Desktop\\colorcap\\LekipMorisien\\PythonScript\\4.jpeg", 'r')


#extract pixels from the image into a list
#starting left to right top to bottom
data = np.array(im)
row = len(data)//2
col = len(data[0])//2

#get the middle pixel of the matrix
middle_pixel = data[row,col]

#output the pixels
print(middle_pixel) #middle pixel in RGB
print('%02x%02x%02x' % tuple(middle_pixel)) #middle pixel in Hex


RGB = ",".join([str(value) for value in middle_pixel])
response = requests.get("https://www.thecolorapi.com/id", params = {"rgb": RGB})
print(response.json()["name"]["value"])


def closest_color():
	color_dictionary = {
	  "Black": [0,0,0],
	  "Gray": [127, 127, 127],
	  "Bordeaux": [136, 0, 21],
	  "Red": [237, 28, 36],
	  "Orange": [255, 127, 39],
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

	colors = np.array(list(color_dictionary.values()))
	color = middle_pixel
	distances = np.sqrt(np.sum((colors-color)**2,axis=1))
	index_of_smallest = np.where(distances==np.amin(distances))
	smallest_distance = colors[index_of_smallest]

	message = "First closest color: "
	print(message + str(list(color_dictionary.keys())[index_of_smallest[0][0]]))


closest_color()


