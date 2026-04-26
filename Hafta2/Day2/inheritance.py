class Person:
    def __init__(self, name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age
        print("Person sınıfı oluşturuldu.")

    def intro(self):
        print(f"Merhaba benim adım {self.name}.")

class student(Person):
    def __init__(self, name, surname, age, number):
        super().__init__(name, surname, age)
        self.number = number

class teacher(Person):
    def __init__(self, name, surname, age, branch):
        super().__init__(name, surname, age)
        self.branch = branch


p1=Person("Ebru", "Aydoğan", 37)
p1.intro()
s1=student("Beril", "Aydoğan", 7, 84)
s1.intro()
t1=teacher("Ayşe", "Koç", 35, "Matematik")
t1.intro()