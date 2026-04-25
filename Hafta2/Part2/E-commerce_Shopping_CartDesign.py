class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Fiyat negatif olamaz!")

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f"{self.name} - {self.price} TL"
    

class ShoppingCart:

    def __init__(self):
        self.items = {}  # {Product: quantity}

    def add_product(self, product, quantity=1):
        for p in self.items:
            if p == product:  # __eq__ burada çalışır
                self.items[p] += quantity
                return
        self.items[product] = quantity

    @property
    def total_price(self):
        total = 0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total

    def __len__(self):
        return len(self.items)

    def __str__(self):
        result = "Sepet:\n"
        for product, quantity in self.items.items():
            result += f"{product.name} x{quantity} - {product.price * quantity} TL\n"
        result += f"Toplam: {self.total_price} TL"
        return result
    

p1 = Product("Telefon", 10000)
p2 = Product("Tablet", 5000)
p3 = Product("Telefon", 10000)

cart = ShoppingCart()

cart.add_product(p1, 2)
cart.add_product(p2, 1)
cart.add_product(p3, 3)  

print(cart)
print(len(cart))        
print(cart.total_price)