import unittest
from Book import *
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

if __name__ == '__main__':
    unittest.main()
