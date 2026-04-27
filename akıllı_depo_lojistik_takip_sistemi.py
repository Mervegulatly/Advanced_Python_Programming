class BaseProduct:

    def __init__(self, _stok_kod, _price, _agirlik, _stok_miktar):
        self._stok_kod = _stok_kod
        self._price = _price
        self._agirlik = _agirlik
        self._stok_miktar = _stok_miktar

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Fiyat negatif olamaz!")
        
    @property
    def agirlik(self):
        return self._agirlik
    
    @agirlik.setter
    def agirlik(self, value):
        if value > 0:
            self._agirlik = value
        else:
            raise ValueError("Ağırlık 0'dan küçük olamaz!")

class ElectronicProduct(BaseProduct):

    def __init__(self, _stok_kod, _price, _agirlik, _stok_miktar, warranty_period):
        super().__init__(_stok_kod, _price, _agirlik, _stok_miktar)
        self.warranty_period = warranty_period

class FoodProduct(BaseProduct):

    def __init__(self, _stok_kod, _price, _agirlik, _stok_miktar, expiry_date):
        super().__init__(_stok_kod, _price, _agirlik, _stok_miktar)
        self.expiry_date = expiry_date

class HazardousProduct(BaseProduct):

    def __init__(self, _stok_kod, _price, _agirlik, _stok_miktar, safety_level):
        super().__init__(_stok_kod, _price, _agirlik, _stok_miktar)
        self.safety_level = safety_level

class InventoryManager:
    
    def __init__(self):
        self.products = {}

    def urun_ekle(self, urun_adi, adet):
        if urun_adi in self.products:
            self.products[urun_adi] += adet
        else:
            self.products[urun_adi] = adet

    def urun_listele(self):
        for urun, adet in self.products.items():
            print(f"{urun}: {adet} adet")

            