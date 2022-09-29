from datetime import date
import sys
sys.path.append('Programming project')
def createdictionaryofallvalues(chosenfile):
    f = open(chosenfile,"r")
    d ={}
    numberofids = 0
    a = f.readline()
    while True:
        tempstorestring = ""
        line0 =f.readline()
        if line0 !="":
            line0list = line0.split()
            for i in range(1,len(line0list)):
                tempstorestring = tempstorestring + line0list[i] + "    "
            d[line0list[0]] = line0list
            numberofids = numberofids +1

        else:
            break
    f.close()
    return d
#reads through the entirety of the chosen file and stores it in a dictionary
#print(createdictionaryofallvalues("logfile.txt"))
#print(createdictionaryofallvalues("database.txt"))

def checkifoverdue(date1,date2):
    tempdate1string = ""
    tempdate2string = ""
    tempmonth1string = ""
    tempmonth2string = ""
    tempyear1string=""
    tempyear2string=""
    namelistofmonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    daysof30list = ["September","April","June","November"]
    daysof31list = ["January", "March", "May", "July", "August", "October", "December"]
    a = 0

    if date1[1]=="/":
        date1="0"+date1
        if date1[4]=="/":
            date1=date1[0]+date1[1]+date1[2] + "0"+ date1[3]+ date1[4]+ date1[5]+ date1[6]+ date1[7]+ date1[8]
    elif date1[4]=="/":
        date1=date1[0]+date1[1]+date1[2] + "0"+ date1[3]+ date1[4]+ date1[5]+ date1[6]+ date1[7]+ date1[8]

    if date2[1]=="/":
        date2="0"+date2
        if date2[4]=="/":
            date2=date2[0]+date2[1]+date2[2] + "0"+ date2[3]+ date2[4]+ date2[5]+ date2[6]+ date2[7]+ date2[8]
    elif date2[4]=="/":
        date2=date2[0]+date2[1]+date2[2] + "0"+ date2[3]+ date2[4]+ date2[5]+ date2[6]+ date2[7]+ date2[8]

    #makes sure that the dates are in the correct format of 01/01/2022 or 11/11/2022 if they are double digits
    for char in range(0,2):
        tempdate1string = tempdate1string + date1[char]
        tempdate2string = tempdate2string + date2[char]
    for char in range(3,5):
        tempmonth1string = tempmonth1string + date1[char]
        tempmonth2string = tempmonth2string + date2[char]
    for char in range(6,10):
        tempyear1string = tempyear1string + date1[char]
        tempyear2string = tempyear2string + date2[char]

    
    #  - int(tempdate1)
    for i in range(0,len(daysof30list)):
        if namelistofmonths[int(tempmonth1string)-1] == daysof30list[i]:
            a = 30
    for i in range(0,len(daysof31list)):
        if namelistofmonths[int(tempmonth1string)-1] == daysof31list[i]:
            a = 31
    if a !=30 and a!=31:
        if int(tempyear1string) % 4 ==0:
            a = 29
        else:
            a = 28
    daysleftinthemonth = a - int(tempdate1string)
    a = 0
    yeargap = False
    if int(tempyear2string)>int(tempyear1string):
        tempmonth2int = int(tempmonth2string) +12
        yeargap= True
    else:
        tempmonth2int = int(tempmonth2string)
    
    tempmonth  = int(tempmonth1string)+1

    for i in range(tempmonth,tempmonth2int):
        if yeargap ==True:
            tempmonth=tempmonth-12
        for j in range(0,len(daysof30list)):
            if namelistofmonths[tempmonth-1] == daysof30list[j]:
                a = 30
        for j in range(0,len(daysof31list)):
            if namelistofmonths[tempmonth-1] == daysof31list[j]:
                a = 31
        if a !=30 and a!=31:
            if int(tempyear1string) % 4 ==0:
                a = 29
            else:
                a = 28

        tempmonth =tempmonth + 1
        daysleftinthemonth = daysleftinthemonth + a
        if yeargap ==True:
            tempmonth=tempmonth+12
        else:
            tempmonth=tempmonth
        a=0
    if (tempdate1string == tempdate2string) and (tempmonth1string == tempmonth2string):
        daysleftinthemonth=0
    if tempmonth1string != tempmonth2string:
        totaldays = daysleftinthemonth + int(tempdate2string)
    else:
        totaldays = int(tempdate2string) - int(tempdate1string)
    totaldays1 = totaldays
    tempyear2int = int(tempyear2string)
    while (tempyear2int==int(tempyear1string)) ==False:
        if totaldays1 <365:
            break
        else:
            tempyear2int = tempyear2int - 1
            if (tempyear2int==int(tempyear1string)) ==False:
                if tempyear2int % 4 ==0:
                    totaldays = totaldays +366
                else:
                    totaldays = totaldays + 365
    if date1 == date2:
        totaldays = 0
    return totaldays
#takes two dates as strings and then outputs the number of days between them

#print(checkifoverdue("12/1/2020","21/2/2020"))
#print(checkifoverdue("11/1/2020","21/04/2021"))
def searchforitem(x,d,userinput):
    #x is the column which is going to be searched in the file
    #userinput is the value which is being searched in column x
    #d represents a dictionary of lists which stores all the values of the file in lists
    newd ={}
    numberofids = 0
    for key in d:
        templist = d[key]
        if templist[x] == userinput:
            newd[numberofids] = d[key] #adds a key to a dictionary if the value in column x matches with the user input
            numberofids = numberofids+1
    return newd
    #takes a dictionary and then checks to see if the 
#print(searchforitem(1,createdictionaryofallvalues("database.txt"),"Fantasy_Fiction"))

def changelogfile(bookid,date):
    d=createdictionaryofallvalues("logfile.txt")
    thed=searchforitem(1,createdictionaryofallvalues("logfile.txt"),bookid)
    #makes a dictionary called thed which stores all the times where a book of a specific ID has been taken out
    thed=searchforitem(3,thed,"0")
    #makes a dictionary of one or no value where the book has not been returned
    #it will be at maximum of one value as no two members can hold the book at the same time unless there is an error in the data
    checkoutdate = list(thed[0])
    #as there is only a maximum of one item in the dictionary it will take the first key in the dictionary and store it as a list

    for keys in d:
        templist = d[keys]
        for i in range(0,len(templist)):
            if templist[1] == bookid and templist[3]=="0":
                templist[3]= date #changes the value of zero to the date as the book has been returned
                d[keys] = templist
                chosenkey = keys

    f=open("logfile.txt","w")
    f.write("ID Book_ID Checkout_Date Return_Date 	Member_ID")
    for keys in d:
        tempstring = "\n"
        templist = d[keys]
        for i in range( 0, len(templist)):
            tempstring = tempstring + templist[i] + "    "
            if i == len(templist) -1:
                #print(tempstring)
                f.write(tempstring)
    f.close()
    #uses the dictionary to rewrite the entire logfile as all the information is stored in it


    a = checkifoverdue(checkoutdate[2],date)
    #print(a) 
    return a
#WARNING: while the code below works it will alter the data in the file which may affect the program
# changelogfile("10","16/12/2021")
def removenamefrombookfile(bookid):
    d = createdictionaryofallvalues("database.txt")
    tempstring = "0"
    
    
    for keys in d:
        templist = d[keys]
        for i in range(0,len(templist)):
            if templist[0] == bookid and templist[5]!="0":
                templist[5]= tempstring
                d[keys] = templist
    
    f=open("database.txt","w")
    f.write("ID 	Genre 		Title 			Author 		Purchase_Date 		Member_ID")
    for keys in d:
        tempstring = "\n"
        templist = d[keys]
        for i in range( 0, len(templist)):
            tempstring = tempstring + templist[i] + "			"
            if i == len(templist) -1:
                #print(tempstring)
                f.write(tempstring)
    #when a book is returned it needs to show in the database that it is no longer in the possesion of a member so it replaces the value with a 0
#WARNING: while the code below works it will alter the data in the file which may affect the program
# removenamefrombookfile("1")


def changebookfile(bookid,memberid):
    d = createdictionaryofallvalues("database.txt")
    tempstring = ""
    for i in range(0,4):
        tempstring = tempstring + memberid[i]
    
    
    for keys in d:
        templist = d[keys]
        for i in range(0,len(templist)):
            if templist[0] == bookid and templist[5]=="0":
                templist[5]= tempstring
                d[keys] = templist
    
    f=open("database.txt","w")
    f.write("ID 	Genre 		Title 			Author 		Purchase_Date 		Member_ID")
    for keys in d:
        tempstring = "\n"
        templist = d[keys]
        for i in range( 0, len(templist)):
            tempstring = tempstring + templist[i] + "			"
            if i == len(templist) -1:
                #print(tempstring)
                f.write(tempstring)
    f.close()
    #when a book is taken out the database needs to be updated to show that the book is currently in possesion of someone other than the library and therefore cannot now be taken out
#WARNING: while the code below works it will alter the data in the file which may affect the program
# changebookfile("1","tchr@lboro.ac.uk")






#print(overduebook("8"))

