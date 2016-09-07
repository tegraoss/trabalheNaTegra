import Book
from readConversor import readme_conversor
from Cart import cart

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
        quantity = ''
        # Voltar para resolver o caso de quantidade a mais
        while not isInt(quantity):
            quantity = readNewBook('quantity')
        quantity = int(quantity)
        book.setQtd(book.qtd - quantity)
        cartBook = Book.book(book.nome,book.autor,book.price, quantity)
        currentCart.addItem(cartBook)
        
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
        print('C - Cart') #todo
        print('D - Delete a book') #todo
        print('E - Exit') #toso
        choose = str(input()).lower()
        if choose == 'a':
            addNewBook()
        elif choose == 'b':
            browseBooks(BooksList, SelectBook)
        elif choose == 'c':
            print('todo')
        elif choose == 'd':
            print('todo')
        elif choose == 'e':
            print('Thank you for using our store \o/')
            exit()
        else:
            print('Invalid option')

    # browseBooks(currentCart.itensList)
