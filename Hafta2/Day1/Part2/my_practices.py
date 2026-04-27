class Product():

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self.price
    
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Fiyat negatif olamaz!")
        
    def __eq__(self, other):  #special method
        return self.name == other.name
    
    def __str__(self):
        return f"{self.name} - {self.price} TL"
    

class ShoppingCard():

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity