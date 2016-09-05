import unittest
from Book import *
from Cart import cart
def fullfilTheCart(newCart):
    newCart.addItem(book('Book1','Name1',10.50,1))
    newCart.addItem(book('Book2','Name2',19.25,1))
    newCart.addItem(book('Book3','Name3',09.75,1))
    newCart.addItem(book('Book4','Name4',15.50,1))
    newCart.addItem(book('Book5','Name5',13.20,1))
    newCart.addItem(book('Book6','Name6',22.00,1))
    return newCart

class TestBookClass(unittest.TestCase):
    def test_setQtd(self):
        newBook = book('Livro Teste', 'Zeca', 0 , 0)
        self.assertTrue(newBook.setQtd(10))
        self.assertTrue(newBook.setQtd(0))
        self.assertFalse(newBook.setQtd(-1))

    def test_setPrice(self):
        newBook = book('Livro Teste', 'Zeca', 0 , 0)
        self.assertTrue(newBook.setPrice(5.55))
        self.assertTrue(newBook.setPrice(0.0))
        self.assertFalse(newBook.setPrice(-1.12))

    def test_removeQuantity(self):
        newBook = book('Livro Teste', 'Zeca', 0 , 10)
        self.assertTrue(newBook.removeQuantity(5))
        self.assertFalse(newBook.removeQuantity(10))
        self.assertTrue(newBook.removeQuantity(5))

class TestCartClass(unittest.TestCase):
    def test_removeItem(self):
        newCart = fullfilTheCart(cart())
        self.assertTrue(newCart.itensList[2])

    def test_calcPrice(self):
        newCart = fullfilTheCart(cart())
        self.assertEqual(newCart.calcPrice(), 90.2)

if __name__ == '__main__':
    unittest.main()
