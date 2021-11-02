#!/usr/bin/env python3
import psutil
import emails
import socket

sender = "automation@example.com"
#change this to your username
recipient = "username@example.com"
body = "Please check your system and resolve the issue as soon as possible."
subject = ""

if psutil.cpu_percent() > 80:
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_email(sender, recipient, subject, body)
    emails.send_email(message)
elif psutil.disk_usage('/').percent < 20:
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_email(sender, recipient, subject, body)
    emails.send_email(message)
elif psutil.virtual_memory().available/(1024.0 ** 2) < 500:
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_email(sender, recipient, subject, body)
    emails.send_email(message)
try:
    socket.gethostbyname("127.0.0.1")
except:
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_email(sender, recipient, subject, body)
    emails.send_email(message)