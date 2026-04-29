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

    @property
    def stok_kodu(self):
        return self._stok_kod
    
    @stok_kodu.setter
    def stok_kodu(self, value):
        if not (isinstance(value, str) and value.startswith("STK-") and value[4:].isdigit() and len(value) == 8):
            raise ValueError("Stok kodu 'STK-1234' formatında olmalıdır")
        self._stok_kod = value


    def calculate_shipping(self):
        shipping = self._price + (self._agirlik * self._stok_miktar)
        return shipping


class ElectronicProduct(BaseProduct):

    def __init__(self, _stok_kod, _price, _agirlik, _stok_miktar, warranty_period):
        super().__init__(_stok_kod, _price, _agirlik, _stok_miktar)
        self.warranty_period = warranty_period

    def calculate_shipping(self):
        return super().calculate_shipping()

class FoodProduct(BaseProduct):

    def __init__(self, _stok_kod, _price, _agirlik, _stok_miktar, expiry_date):
        super().__init__(_stok_kod, _price, _agirlik, _stok_miktar)
        self.expiry_date = expiry_date

    def calculate_shipping(self):
        return super().calculate_shipping()

class HazardousProduct(BaseProduct):

    def __init__(self, _stok_kod, _price, _agirlik, _stok_miktar, safety_level):
        super().__init__(_stok_kod, _price, _agirlik, _stok_miktar)
        self.safety_level = safety_level

def calculate_shipping(self):
        base_shipping = super().calculate_shipping()

        multipliers = {
            "LOW": 1.0,
            "MEDIUM": 1.1,
            "HIGH": 1.25
        }

        return base_shipping * multipliers.get(self.safety_level, 1.0)

class LogisticsProcessor(BaseProduct):
    def calculate_shipping(self):
        LogisticsProcessorPolimorphism = super().calculate_shipping()
        return print(f"Logistic'deki polimorphism : {LogisticsProcessor}")

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

            