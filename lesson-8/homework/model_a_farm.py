class Animal:
    def __init__(self, age:int, gender:bool, name:str):
        self.age=age
        self.name=name
        self.gender="Male" if gender else "Female"

    def make_sound():
        pass
    def sleep():
        pass
    def eat():
        pass

class Cat(Animal):
    def __init__(self, age:int, gender:bool, name:str, meal:str):
        super().__init__(age, name, gender)
        self.meal=meal
    def make_sound(self):
        print("Meow")
    def sleep(self):
        print("Sleeps during the day")
    def eat(self):
        print("Cat eats", self.meal,"\n")

class Dog(Animal):
    def __init__(self, age:int, gender:bool, name:str, meal:str):
        super().__init__(age, name, gender)
        self.meal=meal
    def make_sound(self):
        print("Bark")
    def sleep(self):
        print("Sleeps during the night")
    def eat(self):
        print("Dog eats", self.meal,"\n")

class Duck(Animal):
    def __init__(self, age:int, gender:bool, name:str, meal:str):
        super().__init__(age, name, gender)
        self.meal=meal
    def make_sound(self):
        print("Cruck")
    def sleep(self):
        print("Sleeps during the night")
    def eat(self):
        print("Duck eats", self.meal,"\n") 

cat=Cat(3,False,"simba","mice")
cat.make_sound()
cat.sleep()
cat.eat()

dog=Dog(4,True,"dalton","meat")
dog.make_sound()
dog.sleep()
dog.eat()

duck=Duck(2,False,"noname","rice")
duck.make_sound()
duck.sleep()
duck.eat()