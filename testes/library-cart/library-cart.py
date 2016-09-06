from Book import *
from readConversor import readme_conversor
from Cart import cart

def browseBooks(BooksList,responseMethod):
    for book in BooksList:
        if book.qtd > 0:
            print('Name: ' + book.nome + '\n' + 'Author: '+ book.autor + '\n' + 'Price: R$ ' + str(book.price))
            responseMethod(book)

def SelectBook(book):
    print('Y - Add the book to cart\nEnter - to continue')
    resp = str(input()).lower()
    if resp == 'y' or resp == 'yes':
        print("Quantity: ")
        try:
            while not book.setQtd(int(input())):
                print('Invalid Quantity')
        except:
            print('Quantity Error')
        currentCart.addItem(book)

if __name__ ==  '__main__':
    currentCart = cart()
    BooksList = readme_conversor()
    browseBooks(BooksList, SelectBook)
    print(currentCart.length)
    while(true):
        # Menu
        print('A - Add new book') #todo
        print('B - Browse available books')
        print('C - View your cart') #todo
        print('D - Delete a book') #todo

    # browseBooks(currentCart.itensList)
