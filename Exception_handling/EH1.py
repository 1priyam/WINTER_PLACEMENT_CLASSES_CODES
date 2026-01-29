# try:
#     x=int(input("enter number: "))
#     print(10/x)
# except ZeroDivisionError:
#     print("You cannot divide by zero!")
# except ValueError:
#     print("Enter only number")

#-----------------------------------------------------------------


#EXAMPLE OF ELSE
'''try:
    num = int(input("Enter your number: "))
    print(10/num)
except:
    print("error occured")
else:
    print("No error, program runs successfully")

#-----------------------------------------------------------------

#EXAMPLE OF FINALLY BLOCK
try:
    f=open("movies.txt")
except:
    print("file not found error.")
finally:
    print("Program Finished")


age = int(input("enter your age:"))
if age<18:
    raise ValueError("Age must be 18 or above for vote")
print("you can vote")
'''



#----------------------------------------------------------     CUSTOM ERROR   --------------------------------------------------
'''# it is created to handle a specific problem in a program. 
class LowBalanceError(Exception):  
    #this line creates a custom exception name LowBalanceError pass is used because class cannot be empty in
    # python we dont need to add any logic inside the class right now 
    pass
balance = 500
withdraw = int (input("enter amount: "))
if withdraw>balance:
    raise LowBalanceError("Insufficient balance")
print("withdraw successfully")'''


# ------------------------------------------------------------------------------------------------------------------------------
# try :
#     num = int(input("enter a number :"))
#     print(100/num)
# except:
#     print("error")

'''
try:
    try:
        print(1/0)
    finally:
        print("inner finally")
except ZeroDivisionError:
    print("outer Exception")
finally:
    print("outer finally")
'''

'''def test():
    try:
        return 10
    finally:
        return 20
    
print(test())
'''

# def test():
#     try:
#         return 10
#     finally:
#         return 20
# print(test())

# try:
#     try:
#         x=int("abc")
#     except ValueError:
#         print("inner handled")
#         raise
# except Exception:
#     print("outer handled")


age = int(input("enter ur age: "))
if age<18:
    raise ValueError("Age must be 18 or more")
print("you are eligible")
