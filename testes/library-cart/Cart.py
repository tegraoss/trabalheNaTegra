class cart:
    itensList = []
    length = 0

    def __init__(self):
        self.itensList = []
        self.length = 0

    def addItem(self, newItem):
        self.length += 1
        self.itensList.append(newItem)

    def removeItem(self, itemToBeRemoved):
        try:
            self.length -= 1
            self.itensList.remove(itemToBeRemoved)
            return True
        except:
            return False

    def calcPrice(self):
        totalPrice = 0.0
        for book in self.itensList:
            totalPrice += book.price * book.qtd
        return totalPrice
