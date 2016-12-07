# -*- coding: <UTF-8> -*-
from Book import *
def readme_conversor():
    # This code has a very specific proporse. I will comment to clarify
    try:
        eae = open('README.md','r')
    except e:
        print('Error: Can\'t open file')
    # read entire file
    Readme = str(eae.read())

    # Split the string to list. In Github Markdown '|' is the table tag
    Readme = Readme.split('|')
    # In the middle of table when we do the split there is a | end the end of line
    # them a \n and other | so we have to clean this
    for a in range(Readme.count('\n')): Readme.remove('\n')

    tableList = []
    # Clean the list from trash, position 0 is all the text before the table
    # the next 4 is the header line them the next 4 is the '---' line
    for a in range(9,len(Readme)-1):
        tableList.append(Readme[a])

    bookDb = []
    # Do a list of books objects
    # messing with pointers, almost like C
    for a in range(len(tableList) // 4):
        # get price string from table
        price = tableList[(a * 4) + 2]
        # clean it
        price = price.replace('R$ ', '')
        price = price.replace(',', '.')
        # convert it
        price = float(price)
        # instantiate a book
        newBook = book(tableList[a * 4],tableList[(a * 4) + 1], price, int(tableList[(a * 4) + 3]))
        # append to list
        bookDb.append(newBook)
    return bookDb

if __name__ == '__main__':
    readme_conversor()
