#file = open("data.txt", "mode->r,w,a")
# file = open("students.txt","w")
# file.write("Name: Rahul \n")
# file.write("Course: Python \n")
# file.close()


# file = open("students.txt","r")
# data = file.read()
# print(data)
# file.close()


# with open("students.txt","r") as file:
#     data = file.read()
#     print(data)

# file = open("students.txt","a")
# file.write("marks: 90\n")
# file.close()

# file = open("students.txt","r")
# data = file.reading()
# data2 = file.readlines()
# print(data2)

file2 = open("data.txt","w")
file2.write("Name: Priyam Tiwari\n")
file2.write("city: Lucknow \n")

file2 = open("data.txt","a")
file2.write("age: 20\n")
data3 = file2.readlines()