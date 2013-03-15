#!/usr/bin/python3.2
"""Date:13-08-2012 , Time : 10:13 pm ; Version : 0.02 
   Dedicate to Hiren RNT"""
import time
import os
import webbrowser
urllist=[]
filelist =os.listdir()
allfilelength=len(filelist)
x = 1
y=1
#Search text file
while(x <= allfilelength):
    for i in filelist:
        if i.endswith('.txt') == True:
            urllist.insert(y, i)
            y=y+1
    x=x+1
#remove duplicate value
txt_list=list(set(urllist))
file_no = len(txt_list)
#Display text filelist
string = "+++++++++++++++++++++Text File List+++++++++++++++++++\n"
a=""
z=0
t=0
while (z != (file_no-1) ):
    for m in txt_list:
        q= str(t)+ ". " + m + "\n"
        a= a + q
        t=t+1
    z=z+1
string1=string+a
print(string1)
menu=int(input("Now Press File Number :: "))
#file open and link open section
file_open=open(txt_list[menu])
for x in file_open:
    webbrowser.open(x,new=2)
    time.sleep(10)
print("Finish!")
input()    
