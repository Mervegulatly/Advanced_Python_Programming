from datetime import datetime


# =========================
# BASE CLASS
# =========================
class BaseProduct:
    def __init__(self, stock_code, price, weight, stock_quantity):
        self.stock_code = stock_code
        self.price = price
        self.weight = weight
        self.stock_quantity = stock_quantity

    # --- stock_code ---
    @property
    def stock_code(self):
        return self._stock_code

    @stock_code.setter
    def stock_code(self, value):
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Stok kodu en az 3 karakter olmalı!")
        self._stock_code = value

    # --- price ---
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Fiyat negatif olamaz!")
        self._price = value

    # --- weight ---
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Ağırlık 0'dan büyük olmalı!")
        self._weight = value

    # --- stock_quantity ---
    @property
    def stock_quantity(self):
        return self._stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, value):
        if value < 0:
            raise ValueError("Stok miktarı negatif olamaz!")
        self._stock_quantity = value

    # =========================
    # POLYMORPHISM METHOD
    # =========================
    def calculate_shipping(self):
        return self.weight * 1.5

    def __str__(self):
        return f"{self.stock_code} | Fiyat: {self.price} | Ağırlık: {self.weight} | Stok: {self.stock_quantity}"


# =========================
# ELECTRONIC PRODUCT
# =========================
class ElectronicProduct(BaseProduct):
    def __init__(self, stock_code, price, weight, stock_quantity, warranty_period):
        super().__init__(stock_code, price, weight, stock_quantity)
        self.warranty_period = warranty_period

    def calculate_shipping(self):
        return self.weight * 2 + 10  # elektronik daha pahalı

    def __str__(self):
        return super().__str__() + f" | Garanti: {self.warranty_period} yıl"


# =========================
# FOOD PRODUCT
# =========================
class FoodProduct(BaseProduct):
    def __init__(self, stock_code, price, weight, stock_quantity, expiry_date):
        super().__init__(stock_code, price, weight, stock_quantity)
        self.expiry_date = expiry_date

    def calculate_shipping(self):
        return self.weight * 1.2

    def __str__(self):
        return super().__str__() + f" | SKT: {self.expiry_date}"


# =========================
# HAZARDOUS PRODUCT
# =========================
class HazardousProduct(BaseProduct):
    def __init__(self, stock_code, price, weight, stock_quantity, safety_level):
        super().__init__(stock_code, price, weight, stock_quantity)
        self.safety_level = safety_level

    def calculate_shipping(self):
        return self.weight * 3 + (self.safety_level * 5)

    def __str__(self):
        return super().__str__() + f" | Tehlike Seviyesi: {self.safety_level}"


# =========================
# INVENTORY MANAGER (ITERATOR)
# =========================
class InventoryManager:
    def __init__(self):
        self.products = []
        self.index = 0

    def add_product(self, product):
        self.products.append(product)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        raise StopIteration


# =========================
# LOGISTICS PROCESSOR
# =========================
class LogisticsProcessor:
    def __init__(self, inventory: InventoryManager):
        self.inventory = inventory

    def calculate_cost(self, product: BaseProduct):
        return product.calculate_shipping()

    # =========================
    # GENERATOR METHOD
    # =========================
    def critical_stock(self, threshold=5):
        for product in self.inventory:
            if product.stock_quantity < threshold:
                yield product


# =========================
# CONSOLE APP
# =========================
def main():
    inventory = InventoryManager()
    logistics = LogisticsProcessor(inventory)

    while True:
        print("\n--- AKILLI DEPO SİSTEMİ ---")
        print("1- Ürün Ekle")
        print("2- Ürünleri Listele")
        print("3- Lojistik Hesapla")
        print("4- Kritik Stok Listele")
        print("5- Çıkış")

        choice = input("Seçim: ")

        try:
            # =====================
            # ADD PRODUCT
            # =====================
            if choice == "1":
                print("\nÜrün Tipi:")
                print("1- Elektronik")
                print("2- Gıda")
                print("3- Tehlikeli")

                t = input("Seçim: ")
                code = input("Stok Kodu: ")
                price = float(input("Fiyat: "))
                weight = float(input("Ağırlık: "))
                stock = int(input("Stok: "))

                if t == "1":
                    warranty = int(input("Garanti (yıl): "))
                    product = ElectronicProduct(code, price, weight, stock, warranty)

                elif t == "2":
                    expiry = input("Son Kullanma Tarihi (YYYY-MM-DD): ")
                    product = FoodProduct(code, price, weight, stock, expiry)

                elif t == "3":
                    level = int(input("Tehlike Seviyesi: "))
                    product = HazardousProduct(code, price, weight, stock, level)

                else:
                    print("Geçersiz tip!")
                    continue

                inventory.add_product(product)
                print("Ürün eklendi!")

            # =====================
            # LIST PRODUCTS
            # =====================
            elif choice == "2":
                print("\n--- ÜRÜNLER ---")
                for p in inventory:
                    print(p)

            # =====================
            # LOGISTICS COST
            # =====================
            elif choice == "3":
                code = input("Ürün kodu: ")
                found = False

                for p in inventory:
                    if p.stock_code == code:
                        cost = logistics.calculate_cost(p)
                        print("Lojistik maliyeti:", cost)
                        found = True

                if not found:
                    print("Ürün bulunamadı!")

            # =====================
            # CRITICAL STOCK
            # =====================
            elif choice == "4":
                print("\n--- KRİTİK STOK ---")
                for p in logistics.critical_stock():
                    print(p)

            # =====================
            # EXIT
            # =====================
            elif choice == "5":
                print("Çıkış yapılıyor...")
                break

            else:
                print("Geçersiz seçim!")

        except ValueError as e:
            print("Hata:", e)

        except Exception as e:
            print("Beklenmeyen hata:", e)


# =========================
# RUN PROGRAM
# =========================
if __name__ == "__main__":
    main()