# -*- coding: <UTF-8> -*-
class book:
    Name = ''
    Author = ''
    Price = 0.0
    Qtt = 0
    def __init__(self, n, a, p = 0, q = 0):
        self.Name = n
        self.Author = a
        self.Price = p
        self.Qtt = q

    def setPrice(self,NewPrice):
        if NewPrice >= 0.0:
            self.Price = NewPrice
            return True
        else:
            return False
    def setQtt(self,newQuantity):
        if newQuantity >= 0:
            self.Qtt = newQuantity
            return True
        else:
            return False
    def removeQuantity(self, Quantity):
        try:
            if self.Qtt >= Quantity:
                self.Qtt -= Quantity
                return True
            else:
                return False
        except:
            return False
    def addQuantity(self, Quantity):
        self.Qtt += Quantity
