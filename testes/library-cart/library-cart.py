from Book import *
from readConversor import readme_conversor

def browseBooks:
    for book in BooksList:
        if book.qtd > 0:
            print('Nome: ' + book.nome + '\n' + 'Autor: '+ book.autor + '\n' + 'Price: R$ ' + str(book.price) + '\n')
            str(input())

if __name__ ==  '__main__':
    BooksList = readme_conversor()
