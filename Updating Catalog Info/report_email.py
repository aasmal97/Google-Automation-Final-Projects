#!/usr/bin/env python3
from datetime import date
import reports
import emails
import run

if __name__ == "__main__":
    #generate json
    json_data = run()
    today = date.today()
    body = ""
    for item in json_data:
        body += "name: "+ item["name"] + "<br/>"
        body += "weight: "+f'{item["weight"]}' + " lbs" + "<br/>"
    reports.generate_report("/tmp/processed.pdf", f'Processed Update on {today.month} {today.day}, {today.year}', body)
    sender = "automation@example.com"

    #change this to your username@example.com
    receiver= "username@example.com"
    subject = "Upload Completed - Online Fruit Store"
    message = emails.generate_email(sender, receiver, subject, "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", "/tmp/processed.pdf")
    emails.send_email(message)
