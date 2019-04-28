from PIL import Image
import os


currentDirectory = os.getcwd()

for fileName in os.listdir(currentDirectory):
    if fileName.lower().endswith(".jpg"):
        image = Image.open(fileName)
        width, height = image.size
        factor = 0.30
        width = int(width * factor)
        height = int(height * factor)
        img_anti = image.resize((width, height), Image.ANTIALIAS)
        img_anti.save("resized_" + fileName)
        #print("ancho:%i alto:%i" % (width, height))
