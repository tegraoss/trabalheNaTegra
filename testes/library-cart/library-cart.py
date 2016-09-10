import Book
from readConversor import readme_conversor
from Cart import cart
from subprocess import call

def reviewCart(BOOK):
    print('Enter to continue')
    input()

def cartCheckout(CART):
    print('Review your cart to finalize your shopping')
    print('Enter to continue')
    input()
    browseBooks(CART.ItensList , reviewCart)
    print('Your total purchase is R$ ' + str(CART.calcPrice()))
    print('Want to proceed? (Y)es or (n)o')
    Option = str(input()).lower()
    if Option == 'y' or Option == 'yes':
        # Payment procedure here
        print('Payment Method')
        print('Your book will arive soon!')
        input()
        return True
    else:
        print('Back to Menu\nEnter to Continue')
        input()
        return False

def trabalheNaTegra():
    print('10% discount in books of Martin Fowler')
    DiscountedBooks = 0
    for Item in CurrentCart.ItensList:
        if Item.Author.lower() == 'martin fowler':
            print('\nBook: ' + Item.Name + '\nFrom R$ ' + str(Item.Price))
            Item.setPrice(Item.Price * 0.9)
            print('For R$ ' + str(Item.Price))
            DiscountedBooks += 1
    print('\n' + str(DiscountedBooks) + ' books had its price reduced')

def openSource():
    print('Knoledge must be shared \o/')
    for Item in CurrentCart.ItensList:
        Item.setPrice(0.0)
    print(str(len(CurrentCart.ItensList)) + ' books had its price reduced')

def coupons():
    TryAgain = True
    while TryAgain:
        print('Enter you coupon receive discount or benefits')
        Coupon = str(input())
        if Coupon == 'TrabalheNaTegra':
            trabalheNaTegra()
        elif Coupon == 'OpenSource':
            openSource()
        else:
            print('Invalid Coupon\nTry again? (Y)es or (n)o')
            Option = str(input()).lower()
            if not(Option == 'y') and not(Option == 'yes'):
                TryAgain = False
            else:
                call(['clear'])
    # print('\nEnter to continue')
    # input()


def browseBooks(BooksList,responseMethod):
    if len(BooksList) == 0:
        print('List is currently empty\nEnter to continue')
        input()
        return
    for Item in BooksList:
        if Item.Qtt > 0:
            call(['clear'])
            print('Name: ' + Item.Name + '\nAuthor: '+ Item.Author + '\nPrice: R$ ' + str(Item.Price) + '\nQuantity: ' + str(Item.Qtt))
            responseMethod(Item)

def selectBook(BOOK):
    print('\nY - Add the book to cart\nEnter - to continue')
    Resp = str(input()).lower()
    if Resp == 'y' or Resp == 'yes':
        print("Quantity(" + str(BOOK.Qtt) + " books remaining): ")
        while True :
            Quantity = readNewBook('quantity')
            if isInt(Quantity) and BOOK.removeQuantity(int(Quantity)):
                CartBook = Book.book(BOOK.Name,BOOK.Author,BOOK.Price, int(Quantity))
                break
        CurrentCart.addItem(CartBook)

def alterBook(BOOK):
    print('\nR - Remove book from cart\nE - Edit quantity\nEnter - to continue')
    Resp = str(input()).lower()
    if Resp == 'r':
        for Item in BooksList:
            if Item.Name == BOOK.Name:
                Item.addQuantity(BOOK.Qtt)
                CurrentCart.ItensList.remove(BOOK)
    elif Resp == 'e':
        for Item in BooksList:
            if Item.Name == BOOK.Name:
                break
        while True:
            Quantity = readNewBook('new cart quantity')
            if isInt(Quantity) and int(Quantity) >= 0:
                Quantity = (int(Quantity) - BOOK.Qtt)
                if(Quantity < BOOK.Qtt):
                    updateQuantity(Item, BOOK, Quantity)
                else:
                    updateQuantity(BOOK, Item, Quantity * -1)
                break

def updateQuantity(book,item,quantity):
    if book.removeQuantity(quantity):
        item.addQuantity(quantity)
        return True
    else:
        return False


def isFloat(S):
    try:
        float(S)
        return True
    except:
        return False

def isInt(S):
    try:
        int(S)
        return True
    except:
        return False

def readNewBook(atribute):
    print('\nEnter the ' + atribute + ' of the book: ')
    NewAtribute = str(input())
    return NewAtribute

def addNewBook():
    Name = readNewBook('name')
    Author = readNewBook('author')
    Quantity = ''
    while not isInt(Quantity):
        Quantity = readNewBook('quantity')
    Price = ''
    while not isFloat(Price):
        Price = readNewBook('price')
    try:
        BooksList.append(Book.book(Name, Author, float(Price), int(Quantity)))
        print('Book inserted!\nEnter to continue')
        input()
        return True
    except:
        return False



if __name__ ==  '__main__':
    CurrentCart = cart()
    BooksList = readme_conversor()
    while(True):
        # Menu
        call(['clear'])
        print('######################################################################')
        print('#                       WELCOME TO TEGRA STORE                       #')
        print('######################################################################')
        print('Your cart: ' + str(CurrentCart.Length) + ' itens in cart, total value R$ ' + str(CurrentCart.calcPrice()))
        print('1 - Add new book')
        print('2 - Browse available books')
        print('3 - Cart view')
        print('4 - Buy cart itens')
        print('E - Exit')
        Option = str(input()).lower()
        call(['clear'])
        if Option == 'a' or Option =='1':
            addNewBook()
        elif Option == 'b' or Option == '2':
            print('###################### Select Books to put in your cart ######################')
            browseBooks(BooksList, selectBook)
        elif Option == 'c'  or Option == '3':
            print('###################### View your cart ######################')
            browseBooks(CurrentCart.ItensList, alterBook)
            print('###################### Total price: ' + str(CurrentCart.calcPrice()) + ' ######################')
        elif Option == 'r' or Option == '4':
            coupons()
            if cartCheckout(CurrentCart):
                CurrentCart = cart()
        elif Option == 'e' or Option == '5':
            call(['clear'])
            print('Thank you for using our store \o/')
            exit()
        else:
            print('Invalid option!\nEnter')
            input()
