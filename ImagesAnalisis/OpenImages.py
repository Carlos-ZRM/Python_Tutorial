from PIL import Image
import sys

print("Hola")
path = sys.argv[1]
path = "snakes.jpg"
try:
	img = Image.open(path)
	print("Se abrio imagen")
	print (img.histogram()) 
except IOError:
    print("Error")
