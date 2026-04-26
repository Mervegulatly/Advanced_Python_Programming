# class Cartitem:   #Constructor __init__ ile belirtilir ve parametreler self ile çağırılır.
#     def __init__(self, name, price, quantity):
#         self.name = name      #instances
#         self.price = price
#         self.quantity = quantity

#     #instance method
#     def calculate_total(self):  # Bunu self parametresinden anlayabilirsin. instance olduğu burdan anlaşılır.
#         return self.price*self.quantity

#     def appy_discount(self, rate):
#          self.price = self.price*(1-rate)
#          return self.price

# item1 = Cartitem("Telefon", 10000, 2)
# item2 = Cartitem("Bilgisayar", 70000, 3)
# item3 = Cartitem("Tablet", 20000, 3)

# item1.appy_discount(0.2)
# print(item1.price)  #return ile yazmazsa bu şekilde de kullanılabilir.

# print(item1.name, item1.price, item1.quantity)
# print(item2.name, item2.price, item2.quantity)
# print(item3.name, item3.price, item3.quantity)

# print(item1.calculate_total())
# print(item2.appy_discount(0.2))

# # print(calculate_total(item2.price, item2.quantity))


class CartItem:
    def __init__(self, name, price, quantity):
        #instances
        self.name=name
        self.price=price
        self.quantity=quantity

    #instance methods
    def calculate_total(self):
        return self.price * self.quantity
    
    def appy_discount(self, rate):
        self.price=self.price * (1-rate)
        #return self.price

item1=CartItem("Telefon",80000,2)
item2=CartItem("Bilgisayar",90000,1)
item3=CartItem("Tablet",20000,2)

print(item1.name, item1.price, item1.quantity)
#print(item1.calculate_total())
item1.appy_discount(0.1)
print(item1.price)
#print(item2.name, item2.price, item2.quantity)
#print(item2.calculate_total())
#print(item2.appy_discount(0.2))
#print(item3.name, item3.price, item3.quantity)
#print(item3.calculate_total())
#print(item3.appy_discount(0.2))
