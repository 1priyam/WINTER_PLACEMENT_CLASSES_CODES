# DATA HIDING + CONTROLLED ACCESS 
#BY ___ WE MAKE DATA VARIABLE PRIVATE 

'''class Student:
    def __init__(self,marks):
        self._marks=marks
    def get_marks(self):
        return self._marks
    def set_marks(self,new_marks):
        self._marks=new_marks
s1=Student(100)
s1.set_marks(90)
print(s1.get_marks())
'''

class BackAccount:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient balance")

    def deposit(self, amount):
        self.__balance+=amount

acc = BackAccount(5000)
acc.deposit(100)
print(acc.get_balance())