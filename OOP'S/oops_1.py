# class Student:
#     def __init__(self):
#         print("This is our first constructor  ")
#         self.name="Priyam"

# s1 = Student()
# print(s1.name)



#Syntax for parametrized Constructor
# class Student:
#     # name = "Karan"
#     def __init__(self, Fullname,Marks):
#         self.name = Fullname
#         self.score = Marks
# s1=Student("Avinash",99)
# print(s1.name)
# print(s1.score)


#color model and color no in class
# class Car:
#     def __init__(self,model,color):
#         self.m = model
#         self.c = color

# s2 = Car("tata","black")
# print(s2.m)
# print(s2.c)

# class Car:
#     showroom_name = "XYZ Cars"
#     def __init__(self, modelname, carpiece):
#         self.name=modelname
#         self.price=carpiece

# s1=Car("ALTO-800","200000")
# s2=Car("HONDA-CITY","500000")
# print(s2.name)
# print(s1.name)


#Make a class Student where total_student  a class attribute and after everycount the count is increasing 
'''class Student:
    total_student=0
    def __init__(self,name):
        self.name=name 
        Student.total_student+=1

s1 = Student("Rahul")
s2 = Student("Avinash")
print(s1.name)
print(s2.name)
'''



'''class Student:
    def __init__(self,name):
        self.name=name
    def hello(self):
        print("Welcome", self.name)

    #static method
    @staticmethod                                                                   # SAME FOR EVERY OBJECT                                            
    def college_name():
        print("This is LPU")

s1=Student("Priyam")
s1.hello()
s1.college_name()
'''


#CREATE A CLASS STUDNET IN WHICH THERE ARE OBJECT ATTRIBUTE NAME AND MARKS THEN IT HAS A NORMAL METHOD DISPLAY() IT HAS TO PRINT ("HII , NAME YOUR MARKS IS 'marks'")
'''class Student:
    def __init__(self,name,marks):
        self.name= name
        self.marks = marks
    def display(self):
        print("Hii, ",self.name," Your marks is ",self.marks)

s1=Student("Avinash",98)
s1.display()
'''


# Create a class student use normal method for name, mark and static method for university name
class Student :
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks 

    @staticmethod
    def college_name():
        print("This is LPU ")

s1 = Student("Gautam", 85)
print(s1.name)
print(s1.marks)
s1.college_name()