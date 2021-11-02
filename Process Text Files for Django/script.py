#! /usr/bin/env python3
import os
import requests

workdir = os.path.join("data/", "feedback/")
for file in os.listdir(workdir):
    #open files
    opened_file = open(workdir + file, "r")
    file_lines = opened_file.readlines()
    createDict = {
        "title": "",
        "name": "",
        "date": "",
        "feedback": ""
    }
    count_lines = 1
    #create dictionary read files line by line
    for line in file_lines:
        line_strip = line.strip()
        if count_lines == 1:
            createDict["title"] = line_strip
        if count_lines == 2:
            createDict["name"] = line_strip
        if count_lines == 3: 
            createDict["date"] = line_strip
        if count_lines > 3: 
            createDict["feedback"] = createDict["feedback"] + line_strip
        count_lines = count_lines + 1
  
    #send post request and print error messages if they arise
    feedback_sent = requests.post("http://35.223.74.78/feedback/", data = createDict)
    if(feedback_sent.status_code == 201):
        print("success")
    else: 
        print(feedback_sent.status_code, feedback_sent.text)
    
    #close file after creating Dictionary
    opened_file.close()
   