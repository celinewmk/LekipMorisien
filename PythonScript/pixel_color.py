#function that accepts one pixel from the middle of an image and outputs its color


# TODO this will be read from an image we take instead of reading locally
# import image
from PIL import Image #python image library


#create image obj and open for reading

im = Image.open("C:\\Users\\kkiti\\OneDrive\\Documents\\LekipMorisien\\PythonScript\\2.jpg", 'r')

#extract pixels from the image into a list
#starting left to right top to bottom
image_pixels = list(im.getdata())

#get the middle pixel of the matrix
middle_pixel = image_pixels[len(image_pixels)//2]

#output the pixels
print("IMAGE PIXELS ARRAY HERE!\n")
print(image_pixels)
print("\n")
print("MIDDLE PIXEL HERE!!!\n")
print(middle_pixel)

# problem: we cannot map this pixel to this color need to use an image library that isnt working so i gave up lol