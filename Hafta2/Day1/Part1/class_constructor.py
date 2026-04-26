class Cartitem:   #Constructor __init__ ile belirtilir ve parametreler self ile çağırılır.
    def __init__(self, name, price, quantity):
        self.name = name      #self ile nesnenin içine gömüyoruz
        self.price = price
        self.quantify = quantity

item1 = Cartitem("Telefon", 10000, 2)
item2 = Cartitem("Bilgisayar", 70000, 3)
item3 = Cartitem("Tablet", 20000, 3)



print(item1.name, item1.price, item1.quantify)
print(item2.name, item2.price, item2.quantify)
print(item3.name, item3.price, item3.quantify)

