#! /usr/bin/env python3
import os
import re
import requests

def run():
    #change this to given ip address
    url = "http://35.223.74.78/fruits/"
    workdir = os.path.join("supplier-data/", "descriptions/")
    json_arr = []
    for file in os.listdir(workdir):
        #isolate file name
        if re.search(r"\..*", file):
            #extension of file
            ext = re.search(r"\..*", file).group(0)
            fileName = file[0: len(file) - len(ext)]
        else: 
            fileName = file

        #open files
        opened_file = open(workdir + file, "r")
        file_lines = opened_file.readlines()
        createDict = {
            "name": "",
            "weight": "",
            "description": "",
            "image_name": fileName + ".jpeg"
        }
        count_lines = 1
        #create dictionary read files line by line
        for line in file_lines:
            line_strip = line.strip()
            if count_lines == 1:
                createDict["name"] = line_strip
            if count_lines == 2:
                createDict["weight"] = int(re.search(r'\d+', line_strip).group(0))
            if count_lines > 2: 
                createDict["description"] += line_strip
            count_lines = count_lines + 1
        
        #send post request and print error messages if they arise
        json_sent = requests.post(url, data = createDict)
        if(json_sent.status_code == 201):
            print("success")
        else: 
            print(json_sent.status_code)
        json_arr.append(createDict)
        #close file after creating Dictionary
        opened_file.close()
    return json_arr

