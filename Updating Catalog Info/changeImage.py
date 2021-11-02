#! /usr/bin/env python3
import os, re
from PIL import Image
#change this to added / ip address
working_directory = os.path.join("supplier-data/","images/")
#resize imaged size
size = 600,400
#each image
for img in os.listdir(working_directory):
    #isolate image name
    if re.search(r"\..*", img):
        #extension of file
        ext = re.search(r"\..*", img).group(0)
        #image Name
        imgName = img[0: len(img) - len(ext)]
    else: 
        imgName = img
    #convert img size
    with Image.open(working_directory + img) as im:
        #resize image to 600x400
        im.thumbnail(size)

        #Save image in .jpeg to working directory
        #handles conversion
        rgbImage = im.convert("RGB")
        rgbImage.save(working_directory + imgName + ".jpeg", "JPEG")