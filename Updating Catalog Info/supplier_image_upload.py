#! /usr/bin/env python3
import requests
import os
import re
#change this to given ip address
url = "http://34.121.199.250/upload/"
workdir = os.path.join("supplier-data/", "images/")
for file in os.listdir(workdir):
    if re.search(r"\.jpeg", file):
        #open files
        with open(workdir + file, "rb") as opened_file:
            #send post request and print error messages if they arise
            img_sent = requests.post(url, files = {'file': opened_file})
            if(img_sent.status_code == 201):
                print("success")
            else: 
                print(img_sent.status_code)
        
            #close file after sending request
            opened_file.close()
