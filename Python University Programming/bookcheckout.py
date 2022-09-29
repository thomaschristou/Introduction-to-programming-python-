from datetime import date
import database as thedatabase
def checkinput(thestring):
    #checks that thestring starts with four characters and ends with @lboro.ac.uk
    checker = True
    tempstring = ""
    for char in range(4,len(thestring)):
        tempstring = tempstring+thestring[char]
    if tempstring == "@lboro.ac.uk":
        return True
    else:
        return False
#print(checkinput("coai@lboro.ac.uk"))

def checkmemberisnotholdingoverduebooks(memberID):
    #checks that the person with memberID is not holding any books at present which are overdue
    d = thedatabase.createdictionaryofallvalues("logfile.txt")
    d = thedatabase.searchforitem(4,d,memberID)
    d2 ={}
    booksoverdue = False
    for keys in d:
        totaldays=0
        templist = d[keys]
        if templist[3]=="0":
            totaldays = thedatabase.checkifoverdue(templist[2],date.today().strftime("%d/%m/%Y"))
            #if they have taken a book out then checks if it is still within its lease period
            if totaldays>60:
                booksoverdue = True
                d2[keys] = d[keys]

    return d2
#print(checkmemberisnotholdingoverduebooks("tomc@lboro.ac.uk"))
def appenditemtolist(listofinputs,chosenfile):
    f = open(chosenfile,"a")
    tempstring = "\n"
    if thedatabase.searchforitem(0,thedatabase.createdictionaryofallvalues(chosenfile),listofinputs[0]) =={}: 
        #if the id is not already taken ( other checks done before in program)
        for i in range(0,len(listofinputs)):
            tempstring = tempstring + listofinputs[i] + "	   "
        f.write(tempstring)
        f.close()
        thedatabase.changebookfile(listofinputs[1],listofinputs[4])
        return True
    else:
        f.close()
        return False
#below will print false as it shares the same id as another id which is already in the database
#print(appenditemtolist(["27","9","15/12/2021","16/12/2021","tomc@lboro.ac.uk"],"logfile.txt"))
#while not used in the program to add additional books to the database this can be used to add books to the database
#print(appenditemtolist(["14", "Mythology", "Heroes_of_Olympus","Rick_Riodan","18/01/2015","tchr"],"database.txt"))

