class book:
    nome = ''
    autor = ''
    price = 0.0
    qtd = 0
    def __init__(self, n, a, p = 0, q = 0):
        self.nome = n
        self.autor = a
        self.price = p
        self.qtd = q

    def setPrice(self,newPrice):
        if newPrice >= 0.0:
            self.price = newPrice
            return True
        else:
            return False
    def setQtd(self,newQuantity):
        if newQuantity >= 0:
            self.qtd = newQuantity
            return True
        else:
            return False
    def removeQuantity(self, Quantity):
        try:
            if self.qtd >= Quantity:
                self.qtd -= Quantity
                return True
            else:
                return False
        except:
            return False
    def addQuantity(self, Quantity):
        self.qtd += Quantity
