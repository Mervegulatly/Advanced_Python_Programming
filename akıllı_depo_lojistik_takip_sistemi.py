class BaseProduct:

    def __init__(self, stok_kod, _price, agirlik, stok_miktar):
        self.stok_kod = stok_kod
        self._price = _price
        self.agirlik = agirlik
        self.stok_miktar = stok_miktar

class ElectronicProduct(BaseProduct):

    def __init__(self, stok_kod, _price, agirlik, stok_miktar, warranty_period):
        super().__init__(stok_kod, _price, agirlik, stok_miktar)
        self.warranty_period = warranty_period

class FoodProduct(BaseProduct):

    def __init__(self, stok_kod, _price, agirlik, stok_miktar, expiry_date):
        super().__init__(stok_kod, _price, agirlik, stok_miktar)
        self.expiry_date = expiry_date

class HazardousProduct(BaseProduct):

    def __init__(self, stok_kod, _price, agirlik, stok_miktar, safety_level):
        super().__init__(stok_kod, _price, agirlik, stok_miktar)
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

            