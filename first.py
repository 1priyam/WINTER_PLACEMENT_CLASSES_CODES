'''print("hello world")
a = "Priyam"
print(a)
b = 26
c = 24.6
d = "python"
e=9 > 10
print(b,c,d,e)
print(type(b), type(c), type(d), type(e))'''


'''x = int(input("Enter your age: "))
if(x>=18):
    print('you are eligible to vote')
else:
    print('you are a kid')'''


#CODE OF EVEN AND ODD
'''x = int(input("Enter a no.: "))
if(x%2==0):
    print("even")
else:
    print("odd")

#CODE OF GRADES
marks = int(input("Enter your marks : "))
if(marks>=90):
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >=50:
    print("Grade C")
else:
    print("Fail")



#COMPARING TWO NUMBERS WHICH NO. IS GREATER
a = int(input("Enter the first no. : "))
b = int(input("Enter the second no. : "))

if(a>b):
    print("A is the greater number")
elif(a==b):
    print("Both numbers are equal")
else:
    print("B is the greater numer")




#TRAFFIC LIGHT
l = str(input("Enter the traffic light colour: "))
if(l == "Green"):
    print("You can go")
elif(l == "Yellow"):
    print("Ready")
elif( l == "Red"):
    print("You have to Stop")
else:
    print("Bhag jaa yaha se")





#***********************************************FOR LOOP*************************************************************
for i in range(1,11):
    print(2*i,4*i,10*i)



#PRINT ALL THE ODD NUMBERS BETWEEN 1 TO 15
for i in range(1,16):
    if(i%2!=0):
        print(i)


#PATTERN PRINTING
x = int(input("Enter the number: "))

for i in range (1,x+1):
    print("*"*i)

#********************************************** WHILE LOOP **********************************************************

i = 1
while(i <= 5):
    print(i)
    i+=1


num = int(input("Given the number"))
i=1
while(i<=10):
    print(num , "X" ,i , "=" , num*i)
    i+=1
'''

#**************************************** FUNCTIONS *****************************************************************
#-----------------------------------------------------list-----------------------------------------------------------------------------
'''age=[18,19,23,25,36]
age.reverse()
print("reverse of list:",age)
age.sort()
print("sorted list:",age)
print("length of list:",len(age))
print("max in list:",max(age))
print("sum of list:",sum(age))
print("Avaerge of list:",sum(age)/len(age))
age.append[10]
print("appened list:", age)

'''


'''city = ["mumbai", "jaipur", "delhi", "kolkata", "agra"]
city.reverse()
print("Reverse of list:", city)
city.sort()
print("Sorted list:", city)
print("Length of list:", len(city))
print("Max in list:", max(city)) '''  

#--------------------------------------------------------------tuple------------------------------------------------------------------
'''days=("monday","tuseday","wednesday","friday","saturady","sunday")
print(days)
print("it will show the name of day on list at 0:",days[0])
print("it will show the index no :",days.index('tuseday'))
print("it will count the place:",days.count('monday'))
print("slicing :",days[1:2])
'''

'''friend = ("ram", "shyam", "reeta", "geeta", "nita")
print(friend)
print("show the index at this particular index",friend[0])
print("COunt the position: ",friend.count("reeta"))
print("index: ", friend.index("reeta"))
print("slicing: ", friend[1:3])
'''
#---------------------------------------------------------  SET -----------------------------------------------------

'''num = {10,20,30,40,50}
print(num)
num.add(100)
print(num)
num.update([120,130])
print(num)
#num.remove(175)
num.discard(175)
print(num)
print(num.pop())
'''
#------------------------------------------------------  DICTIONARY  ------------------------------------------------

'''student = {"name":"Rahul","age":21,"city":"delhi","course":"python"}
print(student)
print(student["name"])
#get()
#print(student.get("age"))
print(student.keys())
print(student.values())
print(student.items())
student.update({"age":16,"course":"Django"})
print("after updating :",student)
print(student.pop("city"))
print(student.popitem())
print(len(student))
print("******************************************************************")
dict1 = {"a":2,"b":3}
d2 = dict1.copy()
print(d2)
print("******************************************************************")
dict3 = {"c":4,"d":5}
dict1.update(dict3)
print(dict1)

print("******************************************************************")

mobile={"brand":"samsung","model":"s24","price":75000,"stock":20}
print(mobile)
print(mobile["brand"])
print(mobile.keys())
print(mobile.values())
print(mobile.items())
mobile.update({"price":160000,"model":"s25"})
print("After Updating :",student)
print(mobile.pop("stock"))
print(mobile.popitem())
print(len(mobile))
print("******************************************************************")
'''

#--------------------------------------------------------------------------------------------------------------------
#QUESTION
contact={}
while True:
    print("\n------Contact book---------")
    print("1. Add Contact")
    print("2. view Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. exit")

    choice = input("enter your choice here: ")

    #for adding the contacts
    if choice=="1":
        name = input("Enter name:")
        phone = input("enter phone number: ")
        contact[name] = phone
        print("Contact added successfully")

    #for view contact
    elif choice == "2":
        if contact:
            print("\nsaved contact:")
            for name, phone, in contact.items():
                print(name,":", phone)
        else:
            print("no contact found")

    #for search contact
    elif choice == "3":
        name= input("enter name to search: ")
        if name in contact:
            print("Phone number: ",contact[name])
        else:
            print("contact not found")

    # 4 delte contact
    elif choice == "4":
        name = input("Enter the name you want to delete:")
        if name in contact:
            del contact[name]
            print("contact deleted")
        else:
            print("contact not found")

    # 5 exit
    elif choice=="5":
        print("thank you for using contact book ")
        break
    else:
        print("Invalid choice!! pls try again")


#--------------------------------------------------------------------------------------------------------------------------------------

student = {}
while True:
    print("\n---------------student record system-----------")
    print("1. Add Students")
    print("2. view students")
    print("3. search students")
    print("4. delete students")
    print("5. exit")

    choice = input("enter your choice: ")
    #1. Add Student
    if choice=="1":
        roll=input("enter roll number


    #2. view studens
    elif choice == "2":
        if students:
            print("/n all students: ")
            for roll, info in students.items():
                print("roll:",roll)
                print("name:",info["name"])
                print("course:",info["course"])
        else:
            print("no student record found")

    #3. search student
    elif choice == "3":
        roll = input("enter the roll number to search: ")
        if roll in students:
            print("Name: ", students[roll]["name"])
            print("course: ",students[roll]["course"])
        else:
            print("student not found")

    #4 delete student
    elif choice == "4":
        roll = input("enter the roll number ")
        removed=students.pop(roll,"Not found")
        if removed=="not found":
            print("student not found")
        else:
            print("student deleted successfully")

    #5. exit
    elif choice == "5":
        print("thank you for using student record system")
        break
     else:
        print("Invalid choice")
            
            
    











