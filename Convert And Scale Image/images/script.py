#! /usr/bin/env python3
import os, re
from PIL import Image
#resize imaged size
size = 128,128
#each image
for img in os.listdir("images"):
    #extension of file
    ext = re.search(r"\..*", img).group(0)
    #image Name
    imgName = img[0: len(img) - len(ext)]

    with Image.open(os.path.join("images/",img)) as im:
        #rotate image 90 degrees
        im_rotated = im.rotate(90)
        
        #resize image to 128x128
        im_rotated.thumbnail(size)

        #Save image in .jpeg to /opt/icons folder
        #handles conversion
        rgbImage = im_rotated.convert("RGB")
        rgbImage.save(os.path.join("opt/","icons/",imgName) + ".jpeg", "JPEG")