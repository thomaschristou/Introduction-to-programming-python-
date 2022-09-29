import database as thedatabase
from datetime import date
def booksearch1(x,d,userinput,showoverdue=False):
    if d =={}:
        d = thedatabase.createdictionaryofallvalues("database.txt")
    d = thedatabase.searchforitem(x,d,userinput)
    if showoverdue:
        for key in d:
            d[key]=(d[key],overduebook(d[key][1]))
    return d

def booksearch2(x,d,userinput):
    if d =={}:
        d = thedatabase.createdictionaryofallvalues("logfile.txt")
    d = thedatabase.searchforitem(x,d,userinput)
    return d

def createdictionaryofallvalues(data):
    d =thedatabase.createdictionaryofallvalues(data)
    return d

def overduebook(bookid):
    d= createdictionaryofallvalues("logfile.txt")
    d= thedatabase.searchforitem(1,d,bookid)
    book=list(thedatabase.searchforitem(3,d,"0").items())[0][1]
    checkoutdate = book[2]
    today = date.today().strftime("%d/%m/%Y")
    a = thedatabase.checkifoverdue(checkoutdate,today)
    if a>60 and book[3]=="0":
        b = True
    else:
        b= False
    return b


    #thedatabase.changebookfile(bookid,memberid)
