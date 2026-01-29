'''class Human:                                      #PARENT CLASS
    def eat (self):
        print("Human Can eat")


class Student (Human):                               #CHILD CLASS
    def study(self):
        print("students can study")
s1=Student()
s1.study()
s1.eat()





class Animal:
    def speak(self):
        print(" All Animals Can Speak")

class Dog (Animal):
    def bark(self):
        print("But Dog Only Barks")
s2=Dog()
s2.speak()
s2.bark()




class Nokia:
    def call(self):
        print("YOu can call from it ")

class Iphone(Nokia):
    def internet(self):
        print("You can use Internet from anywhere")

s3=Iphone()
s3.call()
s3.internet()
'''

#***********************************************************************************************************************

class Parent:
    def __init__(self):
        print("this is parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("this is child constructor")

obj=Child()


#***********************************************************************************************************************

#METHOD OVERRIDING
'''class Parent():
    def work(self):
        print("I will go to work")

class Child(Parent):
    def work(self):
        print("I will go to school")

obj=Child()
obj.work()'''


# ******************************************************************  MULTIPLE INHERITANCE  ********************************************************************
'''class teacher:
    def tell(self):
        print("I will teach Python")

class coder(teacher):
    def coding(self):
        print("I will do coding in Python")

class Student(coder):
    def pass_exam(self):
        print("Student has passed the exam")


s1 = Student()

# Accessing all inherited methods
s1.tell()        # from teacher
s1.coding()      # from coder
s1.pass_exam()   # from Student
'''
#***********************************************************************************************************************


# class Parent:
#     def __init__(self):
#         self.__x=10

# class Child(Parent):
#     def show(self):
#         print(self.__x)
# obj=Child()
# obj.show()                                    #prints 10, print 0, #error, #none


#***********************************************************************************************************************

# class Parent:
#     def __init__(self):
#         self.x__=10
# class Child(Parent):
#     def __init__(self):
#         self.__x=20
# obj=Child()
# print(obj.__x)




# class Parent:
#     def __init__(self):
#         self.__x=10                                              #__x (double underscore) makes the variable private
# class Child(Parent):
#     def show(self):
#         print(self._Parent__x)
# obj = Child()
# obj.show()


# class Parent:
#     def __init__(self):
#         self._x=100
# class Child (Parent):
#     def show(self):
#         print(self._x)
# obj=Child()
# obj.show()


#***********************************************************************************************************************


''' Ques - create a class name person(parent) in which name will be private variable thenn you have to make constructor
to set the name. and then make  method get_name to return the name 
class student --> inherit person -->show_name()--> showing name using parent method '''

class Person:
    def __init__(self,name):                                #__init__ used to make constructor
        self.__name=name
    def get_name(self):
        return self.__name
class Student(Person):
    def show_name(self):
        print("my name is", self.get_name())
s1=Student("Karan")
s1.show_name()