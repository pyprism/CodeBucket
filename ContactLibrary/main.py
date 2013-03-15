#!/usr/bin/env python3.2
#===============================================================================
# Date:21-08-2012 Contact Library
#===============================================================================
import sqlite3
con = sqlite3.connect('contact.db')
def indata(name,number):
    '''Part of Input()'''
    data=(
          (name,number)
          )
    with con:
        cur=con.cursor()
        cur.execute("insert into main values(?,?)",data)
def Input():
    '''Input contact into database'''
    try:
        while True:
            nam=input("Enter Full Name : ")
            no=input("Enter Phone Number : ")
            indata(nam,no)
    except KeyboardInterrupt:
        main()
        
def Show():
    '''Show all contact from database'''
    with con:
        cur=con.cursor()
        cur.execute('select * from main')
        a = 1
        while True:
                row = cur.fetchone()
                if row == None:
                    break
                print(a,':',"Name:",row[0],"=> Number:",row[1])
                a=a+1
                
def Print(x):
    with con:
        cur=con.cursor()
        cur.execute(x)
        while True:
            row = cur.fetchone()
            if row == None:
                break
            print("Name=",row[0],"Number=",row[1],)
            
def Search():
    '''Search for contact'''
    try:
        choose = int(input("If you want to search by name press 1 or in the case of number press 2 :"))
        if choose == 1:
            name = input("Enter name:")
            com='select * from main where name like \'' + name + '%\''
            Print(com)
        elif choose == 2:
            number = input("Enter number :")
            com='select * from main where number like \'' + number + '%\''
            Print(com)
        main()
    except KeyboardInterrupt:
        main()
        
def Delete():
    '''Remove any contact'''
    try:
        with con:
            cur=con.cursor()
            choose = int(input("Press 1 for name and 2 for number"))
            if choose == 1:
                delete=input("Enter Name:")
                command='delete from main where name=' +'\''+ delete + '\''
                cur.execute(command)
            elif choose == 2:
                delete=input("Enter Number:")
                command='delete from main where number=' +'\''+ delete + '\''
                cur.execute(command)
            main()
    except KeyboardInterrupt:
        main()
        
def Update():
    '''Update any contact'''
    try:
        with con:
            cur=con.cursor()
            choose = int(input("Press 1 for name and 2 for number"))
            if choose == 1:
                delete=input("Enter Name that you want to replace :")
                replace=input('Enter desired name :')
                command='update main set name=\''+replace+'\'' + 'where name=\''+delete+'\''
                cur.execute(command)
            elif choose == 2:
                delete=input("Enter number that you want to replace :")
                replace=input('Enter desired number :')
                command='update main set number=\''+replace+'\'' + 'where number=\''+delete+'\''
                cur.execute(command)
            main()
    except KeyboardInterrupt:
        main()
        
def main():
    try:
        while True:
            print('################# Availlable Options ##################')
            print('''
                     1.Search for contact
                     2.Input contact into database
                     3.Remove any contact
                     4.Show all contacts from database 
                     5.Update any contact''')
            choosen = int(input("Press option's number : "))
            if choosen == 1:
                Search()
            elif choosen == 2:
                Input()
            elif choosen == 3:
                Delete()
            elif choosen == 4:
                Show()
            elif choosen == 5:
                Update()
            else:
                print("Enter correct option number!!")
    except KeyboardInterrupt:
        print("\nGo to hell....!! :) ")
        exit()                  ##Update : if input == q :
        					    ##                 break	
        					    ##         raise SystemExit
        
if __name__ == "__main__":
    main()
