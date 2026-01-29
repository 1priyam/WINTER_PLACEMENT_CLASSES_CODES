#polymorphism
#poly = many
#morph = form
class Dog:
    def speak(self):
        print("Dog is barking")
class Cat:
    def speak(self):
        print("meow")
class Humans:
    def speak(self):
        print("Human speaks")

obj = Dog()
obj.speak()


#polymorphism questions
class Human:
    def speak(self):
        print("Human is speaking")
class Baby:
    def speak(self):
        print("Baby is crying")
class Dog:
    def speak(self):
        print("Dog is barking")

#polymorphism in action
h = Human()
b = Baby()
d = Dog()

h.speak()
b.speak()
d.speak()

#####

#
class Bike:
    def ride(self):
        print("Bike is moving")
class Truck:
    def ride(self):
        print("Truck is moving")
class Car:
    def ride(self):
        print("Car is moving")

C = Car()
T = Truck()
B = Bike()

C.ride()
T.ride()
B.ride()

###
class Person:
    def role(self):
        print("Hi i am a person")
class Student:
    def role(self):
        print("I am a student")
class Teacher:
    def role(self):
        print("I am a teacher")
class Assistant(Student,Teacher):
    pass

obj = Assistant()
obj.role()
