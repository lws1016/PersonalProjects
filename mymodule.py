class Goods:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return '{}\t{}'.format(self.name, self.price)
