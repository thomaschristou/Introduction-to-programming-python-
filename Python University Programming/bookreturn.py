import database as thedatabase
from datetime import date
def returnbook(bookid,returndate):
    if returndate =="":
        returndate = date.today().strftime("%d/%m/%Y")
    d= thedatabase.createdictionaryofallvalues("logfile.txt")
    d= thedatabase.searchforitem(1,d,bookid)
    if d != {}:
        a =thedatabase.changelogfile(bookid,returndate)
        thedatabase.removenamefrombookfile(bookid)
        return a
#return book takes the book id and return date and then returns it only if it has been taken out and not returned yet
#changes the value in logfile so that it shows the date that it has been returned after it has been checked out and changed the memberid in the database to 
#show that it is no longer in the possesion of someone anymore
#print(returnbook("2",returndate))