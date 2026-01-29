'''class Address:
    def __init__(self,city):
        self.city=city
    def show_address(self):
        print("city:",self.city)

#Student class
class Student:
    def __init__(self,name,city):
        self.name =name
        self.address=Address(city)                            #ACCESING THE OBJECT OF ADDRESS CLASS
        #Creating object of address class inside student class

    def show_student(self):
        print("Name: ",self.name)
        #using object of another class
        self.address.show_address()

s=Student("Karan","Delhi")
s.show_student()


class Engine:
    def start(self):
        print("Engine started")
class Car:
    def __init__(self):
        self.engine=Engine()
    def drive(self):
        self.engine.start()
        print("Car is moving")
obj = Car()
obj.drive()
'''




class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()   # Car HAS-A Engine

    def drive(self):
        self.engine.start()
        print("Car is moving")

c = Car()
c.drive()
