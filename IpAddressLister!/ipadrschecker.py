#!/usr/bin/python3
import urllib.request
import time
time.sleep(3600)
raw = urllib.request.urlopen('http://automation.whatismyip.com/n09230945.asp')
finaldata=str(raw.read())
outputfile=open("iplist","a")
outputfile.write(finaldata + "\n")
print("Finish!!!")
