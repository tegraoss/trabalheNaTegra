# -*- coding: <UTF-8> -*-
class cart:
    ItensList = []
    Length = 0

    def __init__(self):
        self.ItensList = []
        self.Length = 0

    def addItem(self, NewItem):
        self.Length += 1
        self.ItensList.append(NewItem)

    def removeItem(self, ItemToBeRemoved):
        try:
            self.Length -= 1
            self.ItensList.remove(ItemToBeRemoved)
            return True
        except:
            return False

    def calcPrice(self):
        TotalPrice = 0.0
        for Book in self.ItensList:
            TotalPrice += Book.Price * Book.Qtt
        return TotalPrice
