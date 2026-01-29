#Abstraction is the process of hiding implementation details and exposing only the required functionality.
#User focuses on what an object does, not how it does it.


'''class Payment:
    def pay(self,amount):
        pass

class UPI(Payment):
    def pay(self,amount):
        print("Paid using UPI:",amount)

class Card(Payment):
    def pay(self,amount):
        print("Paid using card:",amount)

class Cash(Payment):
    def pay(self,amount):
        print("Paid using cash: ",amount)


obj=UPI()
obj.pay(12)
obj2=Cash()
obj2.pay(500)
obj3=Card()
obj3.pay(50000)
'''

#***************************************************************************************************
 #pass                                         #do nothing syntax error se bachne ke liye

# Abstract class
'''class Shape(ABC):

    @abstractmethod
    def tell(self):
        pass   # abstract method, body nahi hoti


class Circle(Shape):
    def tell(self):
        print("This is a Circle")


class Triangle(Shape):
    def tell(self):
        print("This is a Triangle")


class Rectangle(Shape):
    def tell(self):
        print("This is a Rectangle")


# Object creation
c = Circle()
t = Triangle()
r = Rectangle()

c.tell()
t.tell()
r.tell()
'''



'''
# Abstract class
class Shape(ABC):

    @abstractmethod
    def tell(self):
        pass

    @abstractmethod
    def rules(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def tell(self):
        print("This is a Circle")

    def rules(self):
        print("Rule: A Circle is identified by its radius")
        print("Radius =", self.radius)


class Triangle(Shape):
    def __init__(self, sides):
        self.sides = sides

    def tell(self):
        print("This is a Triangle")

    def rules(self):
        print("Rule: A Triangle has 3 sides")
        print("Sides =", self.sides)


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def tell(self):
        print("This is a Rectangle")

    def rules(self):
        print("Rule: A Rectangle has length and breadth")
        print("Length =", self.length, "Breadth =", self.breadth)


# Object creation
c = Circle(5)
t = Triangle([3, 4, 5])
r = Rectangle(10, 5)

c.tell()
c.rules()

t.tell()
t.rules()

r.tell()
r.rules()
'''






#----------------------------------------------------  INTERFACE  ----------------------------------------------------------------------------
#Abstract class
class Course:                                                              #there are two methods and rulee
    def course_info(self):
        print("This is a programming course")
    def duration(self):
        pass

class ExamInterface:                                                       #there is only rule
    def exam_type(self):
        pass
class PythonCourse(Course,ExamInterface):
    def duration(self):
        print("Course duration is 3 months")
    def exam_type(self):
        print("Exam is a practical based")

c=PythonCourse()
c.course_info()
c.duration()
c.exam_type()
