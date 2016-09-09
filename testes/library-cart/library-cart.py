import Book
import time
from readConversor import readme_conversor
from Cart import cart
from subprocess import call

def TrabalheNaTegra():
    print('10% discount in books of Martin Fowler')
    discountedBooks = 0
    for book in currentCart.itensList:
        if book.autor.lower() == 'martin fowler':
            print('\nBook: ' + book.nome + '\nFrom R$ ' + str(book.price))
            book.setPrice(book.price * 0.9)
            print('\nFor R$ ' + str(book.price))
            discountedBooks += 1
    print(str(discountedBooks) + ' had its price reduced')

def openSource():
    print('Knoledge must be shared \o/')
    for book in currentCart.itensList:
        book.setPrice(0.0)
    print(str(len(currentCart.itensList)) + ' had its price reduced')

def coupons():
    print('Enter you coupon receive discount or benefits')
    coupon = str(input())
    if coupon == 'TrabalheNaTegra':
        TrabalheNaTegra()
    elif coupon == 'OpenSource':
        openSource()
    else:
        print('Invalid Coupon')
    print('\nEnter to continue')
    input()


def browseBooks(BooksList,responseMethod):
    if len(BooksList) == 0:
        print('List is currently empty\nEnter to continue')
        input()
        return
    for book in BooksList:
        if book.qtd > 0:
            call(['clear'])
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
    print('\nEnter the ' + atribute + ' of the book: ')
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
        print('Book inserted!\nEnter to continue')
        input()
        return True
    except:
        return False
if __name__ ==  '__main__':
    currentCart = cart()
    BooksList = readme_conversor()
    while(True):
        # Menu
        call(['clear'])
        print('######################################################################')
        print('#                       WELCOME TO TEGRA STORE                       #')
        print('######################################################################')
        print('Your cart: ' + str(currentCart.length) + ' itens in cart, total value R$ ' + str(currentCart.calcPrice()))
        print('1 - Add new book')
        print('2 - Browse available books')
        print('3 - Cart view')
        print('4 - Enter a Coupon')
        print('E - Exit')
        choose = str(input()).lower()
        call(['clear'])
        if choose == 'a' or choose =='1':
            addNewBook()
        elif choose == 'b' or choose == '2':
            print('###################### Select Books to put in your cart ######################')
            browseBooks(BooksList, SelectBook)
        elif choose == 'c'  or choose == '3':
            print('###################### View your cart ######################')
            browseBooks(currentCart.itensList, alterBook)
            print('###################### Total price: ' + str(currentCart.calcPrice()) + ' ######################')
        elif choose == 'r' or choose == '4':
            coupons()
        elif choose == 'e' or choose == '5':
            call(['clear'])
            print('Thank you for using our store \o/')
            exit()
        else:
            print('Invalid option!\nEnter')
            input()

    # browseBooks(currentCart.itensList)
