import Book
from readConversor import readme_conversor
from Cart import cart
from subprocess import call

def browseBooks(BooksList,responseMethod):
    for book in BooksList:
        if book.qtd > 0:
            print('Name: ' + book.nome + '\nAuthor: '+ book.autor + '\nPrice: R$ ' + str(book.price) + '\nQuantity: ' + str(book.qtd))
            responseMethod(book)

def SelectBook(book):
    print('\nY - Add the book to cart\nEnter - to continue')
    resp = str(input()).lower()
    if resp == 'y' or resp == 'yes':
        print("Quantity(" + str(book.qtd) + " books remaining): ")
        while True :
            quantity = readNewBook('quantity')
            if isInt(quantity) and book.removeQuantity(int(quantity)):
                cartBook = Book.book(book.nome,book.autor,book.price, int(quantity))
                break
        currentCart.addItem(cartBook)

def alterBook(book):
    print('\nR - Remove book from cart\nE - Edit quantity\nEnter - to continue')
    resp = str(input()).lower()
    if resp == 'r':
        for item in BooksList:
            if item.nome == book.nome:
                item.addQuantity(book.qtd)
                currentCart.itensList.remove(book)
    elif resp == 'e':
        for item in BooksList:
            if item.nome == book.nome:
                break
        while True:
            quantity = readNewBook('new cart quantity')
            if isInt(quantity) and int(quantity) >= 0:
                quantity = (int(quantity) - book.qtd)
                if(quantity < book.qtd):
                    updateQuantity(item, book, quantity)
                else:
                    updateQuantity(book, item, quantity * -1)
                break

def updateQuantity(book,item,quantity):
    if book.removeQuantity(quantity):
        item.addQuantity(quantity)
        return True
    else:
        return False


def isFloat(s):
    try:
        float(s)
        return True
    except:
        return False

def isInt(s):
    try:
        int(s)
        return True
    except:
        return False

def readNewBook(atribute):
    print('Enter the ' + atribute + ' of the book: ')
    newAtribute = str(input())
    return newAtribute

def addNewBook():
    name = readNewBook('name')
    author = readNewBook('author')
    quantity = ''
    while not isInt(quantity):
        quantity = readNewBook('quantity')
    price = ''
    while not isFloat(price):
        price = readNewBook('price')
    try:
        BooksList.append(Book.book(name,author, float(price), int(quantity)))
        return True
    except:
        return False

if __name__ ==  '__main__':
    currentCart = cart()
    BooksList = readme_conversor()
    # browseBooks(BooksList, SelectBook)
    # print(currentCart.length)
    while(True):
        # Menu
        print('A - Add new book')
        print('B - Browse available books')
        print('C - Cart')
        print('D - Delete a book') #todo
        print('E - Exit') #todo
        choose = str(input()).lower()
        if choose == 'a':
            addNewBook()
        elif choose == 'b':
            print('###################### Select Books to put in your cart ######################')
            browseBooks(BooksList, SelectBook)
        elif choose == 'c':
            print('###################### View your cart ######################')
            browseBooks(currentCart.itensList, alterBook)
            print('###################### Total price: ' + str(currentCart.calcPrice()) + ' ######################')
        elif choose == 'd':
            print('todo')
        elif choose == 'e':
            call(['clear'])
            print('Thank you for using our store \o/')
            exit()
        else:
            print('Invalid option')

    # browseBooks(currentCart.itensList)
