from tkinter import *
from tkinter import ttk
import sys
sys.path.append('Programming project')
import booksearch as thesearch
def reccomendbooks(genreandauthor,dictionaryofallvalues):
    newdictionary={}
    numberofids = 0
    for key in dictionaryofallvalues:
        templist = dictionaryofallvalues[key]
        if templist[1] == genreandauthor[0] and templist[3] == genreandauthor[1]:
            print(end="")           
        elif templist[1] == genreandauthor[0]:
            newdictionary[numberofids] = dictionaryofallvalues[key]
            numberofids = numberofids+1
        elif templist[3] == genreandauthor[1]:
            newdictionary[numberofids] = dictionaryofallvalues[key]
            numberofids = numberofids+1
    return newdictionary
#creates a new dictionary from a dictionary of all the books with only books that have the same genre or same author as described in the list
#print(reccomendbooks(["Fantasy_Fiction","Shakespeare"],thesearch.createdictionaryofallvalues("database.txt")))

def popularityofbooks(thedictionary):
    counter = 0
    counting = []
    for i in thedictionary:
        templist = thedictionary[i]
        tempstring = templist[0]
        d = thesearch.createdictionaryofallvalues("logfile.txt")
        for i in d:
            secondtemplist = d[i]
            if tempstring == secondtemplist[1]:
                counter = counter +1
        counting.append(counter)
    #counts up number of occurences and places them in a list
    names = []
    for i in thedictionary:
        templist = thedictionary[i]
        tempstring = templist[2]
        names.append(tempstring)
    tuplelist = list(zip(names,counting))
    return tuplelist
#counts up the amount of occurances that each book has in the dictionary in logfile.txt
#print(popularityofbooks(reccomendbooks(["Fantasy_Fiction","J.K.Rowling"],thesearch.createdictionaryofallvalues("database.txt"))))

def returnallgenresforamember(memberID):
    #takes a member id checks for all the books theyve taken out
    #gets all the genres and authors that they have read
    #reccommends books of the same genre or same author as ones they have read
    #matches them with how popular they are and outputs them as a tuplelists
    d = thesearch.booksearch2(4,{},memberID)
    bookstakenout = []
    for keys in d:
        templist = d[keys]
        bookstakenout.append(templist[1])
    bookstakenout = list(dict.fromkeys(bookstakenout))
    listofallgenres = []
    listofallauthors = []
    for i in range(0,len(bookstakenout)):
        newd = thesearch.booksearch1(0,{},bookstakenout[i])
        for key in newd:
            templist1 = newd[key]
            listofallauthors.append(templist1[3])
            listofallgenres.append(templist1[1])
    z={}
    for i in range(0,len(listofallauthors)):
        newd = reccomendbooks([listofallgenres[i],listofallauthors[i]],thesearch.createdictionaryofallvalues("database.txt"))
        z = z|newd #combines dictionary with exiistging dictionary and eliminates common keys
    tuplelist = popularityofbooks(z)
    return tuplelist
#print(returnallgenresforamember("tchr@lboro.ac.uk"))

#print(reccomendbooks(["Fantasy_Fiction","Shakespeare"],thesearch.createdictionaryofallvalues()))
