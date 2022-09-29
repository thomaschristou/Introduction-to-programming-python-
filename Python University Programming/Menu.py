from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import date
import sys
sys.path.append('Programming project')
import booksearch as thesearch
import bookcheckout as thebookcheckout
import bookreturn as thereturn
import bookreccomend as thereccommended
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
multipletabs = ttk.Notebook(root)                                                                                                                                                 

def buttonpressed(IDentry,genreentry,Titleentry,Authorentry,PurchaseDateentry,MemberIdentry,thewidget):
    #takes all the entry boxes and their data so that it can perform the function
    a = {}
    numberofloops = 0
    Checkifsearchalreadycompleted=[False,False,False,False,False,False] #makes suer that the same function is not called multiple times for no reason
    if IDentry.get() == "" and genreentry.get() == "" and Titleentry.get() == "" and Authorentry.get() == "" and PurchaseDateentry.get() == "" and MemberIdentry.get() == "":
        a = thesearch.createdictionaryofallvalues("database.txt")
        #if no value is given the table should be refilled with all values as no constraint is put on the data
    else:
        while numberofloops<5:
            if IDentry.get()!="" and Checkifsearchalreadycompleted[0]==False:
                a=thesearch.booksearch1(0,a,IDentry.get())
                Checkifsearchalreadycompleted[0]=True

            elif genreentry.get()!=""and Checkifsearchalreadycompleted[1]==False:
                tempstring = convertspacestounderscores(genreentry.get())
                a = thesearch.booksearch1(1,a,tempstring)
                Checkifsearchalreadycompleted[1]=True

            elif Titleentry.get()!=""and Checkifsearchalreadycompleted[2]==False:
                tempstring = convertspacestounderscores(Titleentry.get())
                a = thesearch.booksearch1(2,a,tempstring)
                Checkifsearchalreadycompleted[2]=True

            elif Authorentry.get()!=""and Checkifsearchalreadycompleted[3]==False:
                tempstring = convertspacestounderscores(Authorentry.get())
                a = thesearch.booksearch1(3,a,tempstring)
                Checkifsearchalreadycompleted[3]=True

            elif PurchaseDateentry.get()!=""and Checkifsearchalreadycompleted[4]==False:
                a = thesearch.booksearch1(4,a,PurchaseDateentry.get())
                Checkifsearchalreadycompleted[4]=True

            elif MemberIdentry.get()!=""and Checkifsearchalreadycompleted[5]==False:
                a = thesearch.booksearch1(5,a,MemberIdentry.get())
                Checkifsearchalreadycompleted[5]=True
            numberofloops=numberofloops+1
        #loops through 5 times to check that every requirement is met when it is searching for the list of books that satisfy the given requirements
    putnamesintotreeview(thewidget,a,"database.txt")
#function which will update the table with the criteria of the search

def button2pressed(IDentry,genreentry,Titleentry,Authorentry,PurchaseDateentry,MemberIdentry,thewidget):
    #takes all the entry boxes and their data so that it can perform the function
    try:
        a = {}
        Checkifsearchalreadycompleted=[False,False,False,False,False,False]
        numberofloops = 0
        while numberofloops<5:
            if IDentry.get()!="" and Checkifsearchalreadycompleted[0]==False:
                a=thesearch.booksearch1(0,a,IDentry.get())
                Checkifsearchalreadycompleted[0]=True

            elif genreentry.get()!=""and Checkifsearchalreadycompleted[1]==False:
                tempstring = convertspacestounderscores(genreentry.get())
                a = thesearch.booksearch1(1,a,tempstring)
                Checkifsearchalreadycompleted[1]=True

            elif Titleentry.get()!=""and Checkifsearchalreadycompleted[2]==False:
                tempstring = convertspacestounderscores(Titleentry.get())
                a = thesearch.booksearch1(2,a,tempstring)
                Checkifsearchalreadycompleted[2]=True

            elif Authorentry.get()!=""and Checkifsearchalreadycompleted[3]==False:
                tempstring = convertspacestounderscores(Authorentry.get())
                a = thesearch.booksearch1(3,a,tempstring)
                Checkifsearchalreadycompleted[3]=True

            elif PurchaseDateentry.get()!=""and Checkifsearchalreadycompleted[4]==False:
                a = thesearch.booksearch1(4,a,PurchaseDateentry.get())
                Checkifsearchalreadycompleted[4]=True

            elif MemberIdentry.get()!=""and Checkifsearchalreadycompleted[5]==False:
                a = thesearch.booksearch1(5,a,MemberIdentry.get())
                Checkifsearchalreadycompleted[5]=True
            #loops through 5 times to make sure that even if every field is filled out that it will show a book which will represent every single requirement
            numberofloops=numberofloops+1
        templist = a[0]
        #takes the first book which meets all of these requirements and then shows other books like it
        genreandauthorlist=[templist[1],templist[3]]
        a = thereccommended.reccomendbooks(genreandauthorlist,thesearch.createdictionaryofallvalues("database.txt"))
        putnamesintotreeview(thewidget,a,"database.txt")
    except:
        messagebox.showinfo("Error","You must input correct data values to return a result")
        #error for when invalid input is entered

def convertspacestounderscores(dataentry):
    tempstring=""
    for char in dataentry:
        if char ==" ":
            tempstring=tempstring+"_"
        else:
            tempstring=tempstring+char
    return tempstring
    #converts spaces to underscores so that the user does not have to worry about entering data exactly in the same way that it is stored

def treeviewsub(root,columns1):
    thewidget = ttk.Treeview(root,columns=columns1,show="headings",selectmode="extended")#creates the treeview
    for i in columns1:
        thewidget.column(i,anchor="n",width=130)#addseachcolumn from the list
        thewidget.heading(i, text=i,anchor="n")
    return thewidget#returns the treeview table
 
def putnamesintotreeview(thewidget,thedictionary,chosenfile):
    for i in thewidget.get_children():
        thewidget.delete(i)
    #clears the treeview
    x=0
    for i in thedictionary.values():
        tag1 = "blue"
        try:
            if chosenfile == "logfile.txt":
                d =thesearch.booksearch2(3,{},"0")
                book=list(thesearch.booksearch2(0,{},i[0]).items())[0][1]
                #createse a list of all elements from one line of the log file
                if thesearch.overduebook(i[1])==True and book[3]=="0":
                    tag1 = "red"
                    #only highlights the log responsible for the book being overdue and not returned
            else:
                #if the chosenfile is equal to database.txt
                if thesearch.overduebook(i[0]):
                    tag1 = "red"
        except:
            tag1 = "blue"
        thewidget.insert("",index=0,iid=x,values=i,tag=tag1)#inserts the values of the list into the table
        x=x+1
    thewidget.tag_configure("red",foreground="red",font=('', 9, 'bold'))
    #highlights the text as bold if the requirements are met for the book being overdue
#there was an issue with changing the background in the treeview therefore instead the text is bold 
def booksearch():
    frame = Frame()
    blanklabel1 =Label(frame,text="           ",padx=40,pady=10)
    blanklabel2 =Label(frame,text="           ",padx=40,pady=10)
    Titlelabel1 =Label(frame,text="Libary Managemnent system",font='Arial 10 bold underline',padx=40,pady=10)
    blanklabel3 =Label(frame,text="",padx=10,pady=10)
    blanklabel1.grid(row=0,column=2)
    blanklabel2.grid(row=0,column=1)
    Titlelabel1.grid(row=0,column=0)
    blanklabel3.grid(row=0,column=3)
    
    columns1= ['ID', 'Genre', 'Title', 'Author', 'Purchase_Date', 'Member_ID']
    thewidget = treeviewsub(frame,columns1)
    putnamesintotreeview(thewidget,thesearch.createdictionaryofallvalues("database.txt"),"database.txt")
    thewidget.grid(rowspan=6,column=4)
    
    IDlabel=Label(frame,text="ID",padx=40,pady=10)
    IDlabel.grid(row=1,column=0)
    IDentry = Entry(frame,text="")
    IDentry.grid(row=1,column=1)
    #label and entry boxes so the user knows what to enter in each box

    genrelabel=Label(frame,text="Genre",padx=40,pady=10)
    genrelabel.grid(row=2,column=0)
    genreentry = Entry(frame,text="")
    genreentry.grid(row=2,column=1)
    #label and entry boxes so the user knows what to enter in each box

    Titlelabel=Label(frame,text="Title of Book",padx=40,pady=10)
    Titlelabel.grid(row=3,column=0)
    Titleentry = Entry(frame,text="")
    Titleentry.grid(row=3,column=1)
    #label and entry boxes so the user knows what to enter in each box

    Authorlabel=Label(frame,text="Author",padx=40,pady=10)
    Authorlabel.grid(row=4,column=0)
    Authorentry = Entry(frame,text="")
    Authorentry.grid(row=4,column=1)
    #label and entry boxes so the user knows what to enter in each box

    PurchaseDatelabel=Label(frame,text="Purchase Date",padx=40,pady=10)
    PurchaseDatelabel.grid(row=5,column=0)
    PurchaseDateentry = Entry(frame,text="")
    PurchaseDateentry.grid(row=5,column=1)
    #label and entry boxes so the user knows what to enter in each box

    MemberIdlabel=Label(frame,text="Member ID",padx=40,pady=10)
    MemberIdlabel.grid(row=6,column=0)
    MemberIdentry = Entry(frame,text="")
    MemberIdentry.grid(row=6,column=1)
    #label and entry boxes so the user knows what to enter in each box

    mybutton1 = Button(frame,text="Search", padx=40,pady=10, fg="White", bg="Black", 
    command=lambda:buttonpressed(IDentry,genreentry,Titleentry,Authorentry,PurchaseDateentry,MemberIdentry,thewidget))
    mybutton1.grid(row=7,column=1)
    #button that calls a subroutine which will update the table which will return a table of different content based on every single input in the boxed
    #this means that this subroutine can search based on ID or genre or Title of a book or By an Author or by what day it was purchased or any combination of the prior elements
    #additionally if called when all fields are blank then it will return every book that is stored in databse.txt

    mybutton2 = Button(frame,text="Reccomend books", padx=40,pady=10, fg="White", bg="Black", command=lambda:button2pressed(IDentry,genreentry,Titleentry,Authorentry,PurchaseDateentry,MemberIdentry,thewidget))
    mybutton2.grid(row=7,column=0)
    #button that from a book or selection of books that fall under a certain category will return a number of books to be reccomended
    explanationlabel=Label(frame,text="In this table you can search for items based off given inputs. Clicking the book search button will show a list of books which meet those \n \
    requirements. You can search for \"Fantasy Fiction\" or other genres, or by book id or by author or a combination of both. However the text inputted is case sensitive. \
        \nTo show a table with a list of all books make sure every field is empty in the entry boxes and click the Search button. (Enter a member ID in the format of 4 characters) \
        \n Books that are overdue are highlighted in bold. You can also reccomend books with shared properties of given entries by pressing the Reccomend Books button eg memberID = 11 \
        \n (will not include the book which the reccomended books are reccomended by)",padx=40,pady=10)
    explanationlabel.grid(row=7,column=4)

    blanklabel1.grid(row=0,column=2)
    blanklabel2.grid(row=0,column=1)
    Titlelabel1.grid(row=0,column=0)
    blanklabel3.grid(row=0,column=3)
    return frame

def checkoutbuttonpressed(IDentry,bookidentry,checkoutentry,returnentry,memberentry,thewidget):
    if returnentry.get() =="":
        returnentryvariable = "0"
    else:
        returnentryvariable = returnentry.get()
    if checkoutentry.get() =="":
        checkoutentryvariable = date.today().strftime("%d/%m/%Y")
        date1 = checkoutentryvariable
        if date1[1]=="/":
            date1="0"+date1
            if date1[4]=="/":
                date1=date1[0]+date1[1]+date1[2] + "0"+ date1[3]+ date1[4]+ date1[5]+ date1[6]+ date1[7]+ date1[8]
        elif date1[4]=="/":
            date1=date1[0]+date1[1]+date1[2] + "0"+ date1[3]+ date1[4]+ date1[5]+ date1[6]+ date1[7]+ date1[8]
        checkoutentryvariable = date1
    else:
        checkoutentryvariable = returnentry.get()
    #allows for an input of a checkout that has happened in the past which was not recorded but now can be added to the list of logs

    adictionaryofchosenvalues = thesearch.booksearch2(1,{},bookidentry.get())
    adictionaryofchosenvalues = thesearch.booksearch2(3,adictionaryofchosenvalues,"0")
    #check to see if the book has already been taken out

    books1tring = ""
    d2 =thebookcheckout.checkmemberisnotholdingoverduebooks(memberentry.get())
    for keys in d2:
        templist = d2[keys]
        bookdictionary =thesearch.booksearch1(0,{},templist[1])
        booklist = bookdictionary[0]
        bookstring = booklist[2]
        books1tring = books1tring + bookstring + " , "
    #creates a string of book/s if the member that is requesting the book must return before they are allowed to take out another book

    seconddictionaryofchosenvalues = thesearch.createdictionaryofallvalues("database.txt")
    seconddictionaryofchosenvalues =thesearch.booksearch1(0,{}, bookidentry.get())
    #makes a dictionary of one element to check that the book exists
    if seconddictionaryofchosenvalues !={}:
        #checks the book exists
        if thebookcheckout.checkinput(memberentry.get())==True:
            #gets the content of the memberentry box and checks that the memberentry is in line with the requirements (starts with 4 letters and ends with @lboro.ac.uk)
            if len(adictionaryofchosenvalues)==0:
                #checks to see if the book has already been taken out
                newlist = [IDentry.get(),bookidentry.get(),checkoutentryvariable,returnentryvariable,memberentry.get()]
                #gets a list of all the entries into the box so that it can be appended to the logfile
                #checks that the memberentry 
                if d2 =={}:
                    #checks that there is no book which the user has not returned yet which is overdue
                    if thebookcheckout.appenditemtolist(newlist,"logfile.txt")==False:
                        #if it returns true then the item will display in treeview as successfully appended
                        messagebox.showinfo("Error","The ID needs to be unique")
                        #if the function appenditemtolist returns false then the last input which could be invalid is the ID of the log 
                else:
                    messagebox.showinfo("Error","This user is trying to check out a book when the following books are missing: \n"+books1tring)
                a = thesearch.createdictionaryofallvalues("logfile.txt")
                putnamesintotreeview(thewidget,a,"logfile.txt")
                #will update the table at this point as sufficient check are done
            else:
                messagebox.showinfo("Error","The book you have tried to check out is already withdrawn/hasn't been returned")
        else:
            messagebox.showinfo("Error","Invalid member_ID. Member_ID must be four letters followed by @lboro.ac.uk")
    else:
        messagebox.showinfo("Error","The ID of the book searched does not exist")

def bookcheckout():
    frame = Frame()
    blanklabel1 =Label(frame,text="           ",padx=40,pady=10)
    blanklabel2 =Label(frame,text="           ",padx=40,pady=10)
    Titlelabel1 =Label(frame,text="Withdrawl system",font='Arial 10 bold underline',padx=40,pady=10)
    blanklabel3 =Label(frame,text="",padx=10,pady=10)
    blanklabel1.grid(row=0,column=2)
    blanklabel2.grid(row=0,column=1)
    Titlelabel1.grid(row=0,column=0)
    blanklabel3.grid(row=0,column=3)
    
    columns2= ['ID','Book_ID','Checkout_Date','Return_Date', 'Member_ID',]
    thewidget = treeviewsub(frame,columns2)
    putnamesintotreeview(thewidget,thesearch.createdictionaryofallvalues("logfile.txt"),"logfile.txt")
    thewidget.grid(rowspan=6,column=4)
    #puts in all the logs into the treeview table when the program is first run
    
    IDlabel=Label(frame,text="ID",padx=40,pady=10)
    IDlabel.grid(row=1,column=0)
    IDentry = Entry(frame,text="")
    IDentry.grid(row=1,column=1)
    #label and entry boxes so the user knows what to enter in each box

    bookidlabel=Label(frame,text="Book_ID",padx=40,pady=10)
    bookidlabel.grid(row=2,column=0)
    bookidentry = Entry(frame,text="")
    bookidentry.grid(row=2,column=1)
    #label and entry boxes so the user knows what to enter in each box

    Checkoutdate=Label(frame,text="Check-out date",padx=40,pady=10)
    Checkoutdate.grid(row=3,column=0)
    Checkoutentry = Entry(frame,text="")
    Checkoutentry.grid(row=3,column=1)
    #label and entry boxes so the user knows what to enter in each box

    Returndate=Label(frame,text="Return date",padx=40,pady=10)
    Returndate.grid(row=4,column=0)
    Returnentry = Entry(frame,text="")
    Returnentry.grid(row=4,column=1)
    #label and entry boxes so the user knows what to enter in each box

    Returndate=Label(frame,text="Member_ID",padx=40,pady=10)
    Returndate.grid(row=5,column=0)
    memberentry = Entry(frame,text="")
    memberentry.grid(row=5,column=1)
    #label and entry boxes so the user knows what to enter in each box

    mybutton1 = Button(frame,text="Checkout book", padx=40,pady=10, 
    fg="White", bg="Black",
    command=lambda:checkoutbuttonpressed(IDentry,bookidentry,Checkoutentry,Returnentry,memberentry,thewidget))
    mybutton1.grid(row=6,column=1)
    #button which checks out the books and takes the input from every entry box and adds it to the function
    explanationlabel=Label(frame,text="Enter information into the boxes to check out a book. If the check-out date box is empty then it will return todays date to the program\
        \n If the return book field is empty then it will return a 0 as the return date hasnt been confirmed and therefore is no longer in the libarys possession. Logfile IDs must be unique \
        \n and +1 of the ID at the top. If the book entered is not available it will not allow the book to be checked out. In addition if the member is not able to take out books as  \
        \n they have overdue books it will not allow the book to be checked out. Member IDs must be entered in the format of 4 characters followed by \"@lboro.ac.uk\"",padx=40,pady=10)
    explanationlabel.grid(row=7,column=4)
    return frame

def returningbooks():
    frame = Frame()
    blanklabel1 =Label(frame,text="           ",padx=40,pady=10)
    blanklabel2 =Label(frame,text="           ",padx=40,pady=10)
    Titlelabel1 =Label(frame,text="Libary Managemnent system",font='Arial 10 bold underline',padx=40,pady=10)
    blanklabel3 =Label(frame,text="",padx=10,pady=10)
    blanklabel1.grid(row=0,column=2)
    blanklabel2.grid(row=0,column=1)
    Titlelabel1.grid(row=0,column=0)
    blanklabel3.grid(row=0,column=3)
    #ID Book_ID Checkout_Date Return_Date 	Member_ID
    columns1= ['ID', 'Book_ID', 'Checkout_Date', 'Return_Date', 'Member_ID']
    #names of the headers of the columns
    thewidget = treeviewsub(frame,columns1)
    putnamesintotreeview(thewidget,thesearch.createdictionaryofallvalues("logfile.txt"),"logfile.txt")
    #puts in all the logs into the treeview table when the program is first run
    thewidget.grid(rowspan=6,column=4)
    
    IDlabel=Label(frame,text="Book_ID",padx=40,pady=10)
    IDlabel.grid(row=1,column=0)
    IDentry = Entry(frame,text="")
    IDentry.grid(row=1,column=1)
    #label and entry boxes so the user knows what to enter in each box

    returndate=Label(frame,text="Return Date",padx=40,pady=10)
    returndate.grid(row=2,column=0)
    returndateentry = Entry(frame,text="")
    returndateentry.grid(row=2,column=1)
    #label and entry boxes so the user knows what to enter in each box
    Returnbutton=Button(frame,text="Return Book",padx=40,pady=10, 
    command=lambda:returnbooks(IDentry.get(),returndateentry.get(),thewidget,
    thesearch.createdictionaryofallvalues("logfile.txt")))
    #gets a dictionary of all values in the log file and returns to return book the contents of the two boxes
    Returnbutton.grid(row=3,column=1)
    explanationlabel=Label(frame,text="Enter the book ID of the book you want to return. If the Return Date field is empty then the program will take todays date as the return date",padx=40,pady=10)
    explanationlabel.grid(row=7,column=4)
    
    return frame
#creates a frame which is part of the UI to allow the user to return books with only the bookID and then updates the table to show that it has been returned when the button  is pressed
def returnbooks(bookid,returndate,thewidget,thedictionary):
    #calls the function in bookreturn.py to see how long the book is overdue when it is returned
    d1=thesearch.booksearch2(1,{},bookid)
    d2=thesearch.booksearch2(3,d1,"0") #checks to see if book is available
    try:
        if d1!={} and d2!={}: 
            b = thereturn.returnbook(bookid,returndate)
            if b <60:
                messagebox.showinfo("Success","Book Returned within "+ str(b) +" days.") 
                #outputs how many days it has been gone for since it has been taken out
            else:
                messagebox.showinfo("Success","Book returned. However this book has been taken out for "+ str(b) +"days which exceeds 60 days") 
                #outputs how many days it has been gone for since it has been taken out
        else:
            messagebox.showinfo("Error","Book is available or Book ID does not exist")
    except:
        messagebox.showinfo("Error","Ensure the book that you have entered is correct")
    putnamesintotreeview(thewidget,thesearch.createdictionaryofallvalues("logfile.txt"),"logfile.txt")
#subroutine for showing wether or not a book is able to be returned and checks wether if it is late or not and then will refresh the treeview table in the widget for returning books
#return date is set to todays current date if the user does not want to enter a date
#i believed adding an extra box to add in dates will account for times for example if a computer stops working for a day and the librarian has to enter the books that have been returned
#as being returned on the wrong day if it is only able to be returned on the computers current date

def show(multipletabs,choice):
    multipletabs.select(choice)
#subroutine that takes the user to their selected tab based on what button they press

def drawgraph(frame,memberID):
    figure = plt.Figure(figsize=(10,6))
    figurecanvas = FigureCanvasTkAgg(figure,master=frame)
    figurecanvas.get_tk_widget().grid(row=5,column=2)
    bargraph=figure.add_subplot(1,1,1)
    tuplelist = thereccommended.returnallgenresforamember(memberID)
    #creates a list of tuples from the function with the format of [(bookname,number of times the book has taken out)]
    booknames = []
    timestakenout = []
    for i in range(0,len(tuplelist)):
        (a,b) = tuplelist[i]
        booknames.append(a)
        timestakenout.append(b)
    #this loop converts the outputs from the tuple list and converts them into two seperate lists which will be used for the columns of the bargraph
    bargraph.bar(booknames,timestakenout)
    figurecanvas.draw()
    return figurecanvas
#this is the function which draws the bar graph inside the frame of the reccomended books tab. The graph takes the memberID and if it is a valid memberID and has a history of taking out
#books then it will return a bar graph composed of books that fall under the same genre or has been written by the same author as one of the books which have been taken out

def reccomendbooks():    
    frame = Frame()
    blanklabel1 =Label(frame,text="           ",padx=40,pady=10)
    blanklabel2 =Label(frame,text="           ",padx=40,pady=10)
    Titlelabel1 =Label(frame,text="Reccomend Books",font='Arial 10 bold underline',padx=40,pady=10)
    blanklabel3 =Label(frame,text="",padx=10,pady=10)
    blanklabel1.grid(row=0,column=2)
    blanklabel2.grid(row=0,column=1)
    Titlelabel1.grid(row=0,column=0)
    blanklabel3.grid(row=0,column=3)

    MemberId=Label(frame,text="Member_ID",padx=40,pady=10)
    MemberId.grid(row=1,column=0)
    memberentry = Entry(frame,text="")
    memberentry.grid(row=1,column=1)
    explanationlabel=Label(frame,text="Enter a member ID in the format of 4 characters followed by \"@lboro.ac.uk\" (eg tchr@lboro.ac.uk) to return reccomended \
        \n books for the member into the bargraph",padx=40,pady=10)
    explanationlabel.grid(row=5,column=1)

    Button3 = Button(frame, text="Reccomend Books",padx=69,pady=10,command=lambda:drawgraph(frame,memberentry.get()))
    Button3.grid(row=3,column=1)
    return frame
#reccomendbooks() is a function that returns a frame into mainmenu to display a User interface composed of labels buttons an an entry box. The entry box takes librarians's data entry 
# through the memberentry box and outputs a number of reccomended books in a bar graph after the button is pressed based to show reccomended books for the member which is inputted based 
# off its popularity and how many times it has been taken out
def mainmenu():
    multipletabs.pack(pady=15)
    mainmenuframe = Frame(multipletabs,width=500,height=500)
    Booksearchframe= booksearch()
    Checkingoutbooks = bookcheckout()#Frame(multipletabs,width=500,height=500)
    Returningbooks = returningbooks()
    reccomendingbooks = reccomendbooks()
    #frames created from the functions are returned into the main subroutine and added to the user inteface 
    mainmenuframe.pack(fill="both", expand=1)
    Booksearchframe.pack(fill="both", expand=1)
    Checkingoutbooks.pack(fill="both", expand=1)
    Returningbooks.pack(fill="both", expand=1)
    reccomendingbooks.pack(fill="both", expand=1)

    
    multipletabs.add (mainmenuframe, text="Main Menu")
    multipletabs.add (Booksearchframe, text="Book Search")
    multipletabs.add (Checkingoutbooks, text="Checking out books")
    multipletabs.add (Returningbooks, text="Returning books")
    multipletabs.add (reccomendingbooks, text="Reccomendingbooks")
    
    blanklabel1 =Label(mainmenuframe,text="           ",padx=40,pady=10).grid(row=0,column=0)
    blanklabel2 =Label(mainmenuframe,text="           ",padx=60,pady=10).grid(row=0,column=1)
    thelabel = Label(mainmenuframe,text="Librarian Program",padx=60,pady=10)
    thelabel.grid(row=0,column=1)

    Button1 = Button(mainmenuframe, text="Search for books",padx=60,pady=10,command=lambda:show(multipletabs,1))
    Button1.grid(row=1,column=1)
    Button2 = Button(mainmenuframe, text="Check out books",padx=60,pady=10,command=lambda:show(multipletabs,2))
    Button2.grid(row=2,column=1)
    Button3 = Button(mainmenuframe, text="Return books",padx=69,pady=10,command=lambda:show(multipletabs,3))
    Button3.grid(row=3,column=1)
    Button4 = Button(mainmenuframe, text="Reccommend books",padx=50,pady=10,command=lambda:show(multipletabs,4))
    Button4.grid(row=4,column=1)
    
    explanationlabel=Label(mainmenuframe,text="To choose a section click on one of the buttons above or click on the tabs above to navigate between tasks to be performed",padx=40,pady=10)
    explanationlabel.grid(row=5,column=1)

    root.mainloop()
# main menu sets up the main part of the program, it consists of buttons and implements a notebook which alows for multiple different tabs consisting of frames to be navigated to. It uses 
# tkinter functions to make buttons which make use of the subroutine which will navigate the librarian to the appropriate tab when used. When mainmenu() is called it takes no argurments 
# and is the only subroutine called to make the whole program run.
mainmenu()
