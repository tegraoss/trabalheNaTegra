class cart:
    itensList = []
    numberOfItens = 0

    def __init__(self):
        self.itensList = []
        self.numberOfItens = 0

    def addItem(self, newItem):
        self.itensList.append(newItem)

    def removeItem(self, itemToBeRemoved):
        try:
            self.itensList.remove(itemToBeRemoved)
            return True
        except:
            return False

    def calcPrice(self):
        price = 0
        for item in self.itensList:
            price += item.price
        return price
