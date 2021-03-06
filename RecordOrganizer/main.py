#!/usr/bin/python3.2
#Date : Dec 5 ,2012 ,Its the 1st program  after 3 months , last date of programming August 21 ,Missing RST # 
from os import listdir , mkdir ,path,chdir,getcwd
import shutil

def find_month_name(month):
    if month == '01':
        name_month = 'January'
    elif month == '02':
        name_month = "February"
    elif month == '03':
        name_month = 'March'
    elif month == '04':
        name_month = 'April'
    elif month == '05':
        name_month = 'May'
    elif month == '06' :
        name_month = 'June'
    elif month == '07':
        name_month = 'July'
    elif month == '08':
        name_month = 'August'
    elif month == '09':
        name_month = 'September'
    elif month == '10':
        name_month = 'October'
    elif month == '11':
        name_month = 'November'
    elif month == '12' :
        name_month = 'December'
    return name_month
    
filelist=listdir()
source=getcwd()
for i in filelist:
    if i.endswith('.wav') == True:
        filename = i
        splitname = filename.split('_')
        print(splitname)
        name = splitname[0]
        date = splitname[1]
        year=date[1:5]
        temp_month=date[5:7]
        #Folder Create
        if path.isdir(name) == True:
            chdir(name)
        else:
            mkdir(name)
            chdir(name)
        if path.isdir(year) == True:
            chdir(year)
        else:
            mkdir(year)
            chdir(year)
        month = find_month_name(temp_month)
        if path.isdir(month) == True:
            chdir(month)
            destination_dir = getcwd()
        else:
            mkdir(month)
            chdir(month)
            destination_dir = getcwd()
        source_dir = source + "/" + filename
#Check if file exit or not then move the file
        try:
            shutil.move(source_dir,destination_dir)
            chdir(source)
        except shutil.Error:
            print(" \" {} \" already exits".format(filename))
            pass
