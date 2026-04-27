# class Product():
#     def __init__(self, name, price):
#         self.name = name
#         if price > 0:
#             self.price = price
#         else:
#             raise ValueError("Ürün fiyatı 0'dan düşük olamaz!")

# p1 = Product("Telefon", 10000)

# p1.price = -90000  #Bu şekilde hatalı sonuç döner - leri engelleyemeyiz.

# print(p1.name, p1.price)


#PYTHON'DA erişim kontrolleri _, __ gibi işaretlerle olur public veya, private yerine


class Product:
    def __init__(self, name, price):
        self.name=name
        self._price=price
        # if price > 0:
        #     self._price=price
        # else:
        #     raise ValueError("Ürün fiyatı 0'dan düşük olamaz!")
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value > 0:
            self._price=value
        else:
            raise ValueError("Ürün fiyatı 0'dan düşük olamaz!")
    
    # def set_price(self, value):
    #     if value > 0:
    #         self._price=value
    #     else:
    #         raise ValueError("Ürün fiyatı 0'dan düşük olamaz!")
    
    # def get_price(self):
    #     return self._price



p1=Product("Telefon", 80000)

#p1.price = -90000

print(p1.name, p1.price)

