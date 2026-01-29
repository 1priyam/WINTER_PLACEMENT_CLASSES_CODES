#to create a list 
#number = [10,20,30,40]
#looping through the list 

# for i in number:
#     print(i)

# fruit = []
# print(fruit)
# fruit.append("apple")                         #append is used to add element in list 
# print(fruit)

#QUES- FIND THE SUM OF ALL ELEMENT IN A LIST 

numbers=[5,10,15]
total = 0
for i in numbers:
    total=total+i
print(total)
print("************************************************")


#QUES- Reverse a list
nums = [1,2,3,4]
reverse_list = nums[::-1]
print(reverse_list)
print("************************************************")

#Ques- Remove duplicate element from the list
nums = [1,2,2,3,4,4]
unique = []
for i in nums:
    if i not in unique:
        unique.append(i)
print(unique)
print("************************************************")

#  -------------------------------------------------------------------------     TUPLE    -----------------------------------------------------------------------------\
colors = ("red","green","blue")
print(colors[1])
print(colors[2])

print("************************************************")

#CONVERSION OF LIST INTO TUPLE 
numbers = [1,2,3,4]
print(type(numbers))
num_tuple = tuple(numbers)
print(type(num_tuple))

print("************************************************")

#CONVERSION OF TUPLE IN TO LIST
colors = ("red", "green", "blue")
print(type(colors))
colors_list = list(colors)
print(type(colors_list))

print("************************************************")
#Cnversion of list into a set
nums = [1,1,2,3,3,4]
nums_set = set(nums)
print(nums_set)
nums_list = list(nums_set)
print(nums_list)

print("************************************************")

#Conversion of Dictionary into a set
student = {"name":"karan","age":24}
student_set = set(student)
print(type(student_set))
print(student_set)

print("************************************************")

#Conversion of set into a dictionary
subjects = ("maths", "science", "english")
subject_dict = dict.fromkeys(subjects,100)
print(subject_dict)
print(type(subject_dict))