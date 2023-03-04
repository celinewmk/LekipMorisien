#function that accepts one pixel from the middle of an image and outputs its color


# TODO this will be read from an image we take instead of reading locally
# import image
from PIL import Image #python image library
import numpy as np
import requests

#create image obj and open for reading

im = Image.open("C:\\Users\\kkiti\\OneDrive\\Documents\\LekipMorisien\\PythonScript\\3.jpg", 'r')

#extract pixels from the image into a list
#starting left to right top to bottom
image_pixels = list(im.getdata())
data = np.array(im)
row = len(data)//2
col = len(data[0])//2

#get the middle pixel of the matrix
middle_pixel = image_pixels[row,col]

#output the pixels
print("IMAGE PIXELS ARRAY HERE!\n")
print(image_pixels)
print("\n")
print("MIDDLE PIXEL HERE!!!\n")
print(middle_pixel)

RGB = ",".join([str(value) for value in middle_pixel])
response = requests.get("https://www.thecolorapi.com/id", params = {"rgb": RGB})
print(response.json()["name"]["value"])

# problem: we cannot map this pixel to this color need to use an image library that isnt working so i gave up lol