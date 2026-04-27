class Person:
    def __init__(self, name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age
        print("Person sınıfı oluşturuldu.")

    def intro(self):
        print(f"Merhaba benim adım {self.name}.")

print(type(Person))

# Meta class kullnmazsak her sınıf için değişecek şeyleri manuel tek tek kontrol etmemiz gerekebilir.
# MetaClass sınıf oluşturulduğu an (daha class instance bile yokken) devreye girer.
# En genel ve hepsinin üstüne geçen genel geçer bir class olarak düşünebilirsin