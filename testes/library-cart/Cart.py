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
        price = 0
        for item in self.itensList:
            price += item.price
        return price