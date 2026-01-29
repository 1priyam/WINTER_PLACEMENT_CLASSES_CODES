# print(True+True+False)
# print("5"+"4")
# print("5"*10)


# def change(x):
#     x+=10
# a=5
# change(a)
# print(a)


# def update(lst):
#     lst.append(10)
# nums = [1,2,3]
# update(nums)
# print(nums)


# t=(1,2,3)
# t=t+(4,)
# print(t)


# s={1,2,2,3,3}
# print(len(s))


# i = 1
# while i<10:
#     i*=3
#     print(i)


# for i in range (3):
#     print(i)
# else:
#     print("done")


# try:
#     print("A")
#     10/0
#     print("B")
# except:
#     print("C")
# print("D")


# try:
#     print(1)
# except:
#     print(2)
# finally:
#     print(3)



# def test():
#     try :
#         return 10
#     finally:
#         return 20
# print(test())


#Ques-1 MOVE ALL THE ZEROS TO THE END
'''nums=[0,1,0,3,12]
result=[]     #we will store non elements
zero_count=0
for n in nums:
    if n==0:
        zero_count+=1
    else:
        result.append(n)
    
for i in range (zero_count):
    result.append(0)
print(result)
'''


'''text = "naman"
left=0
right=len(text)-1
isPalindrome=True
while left<right:
    if text[left] != text[right]:
        isPalindrome=False
        break
    left+=1
    right-=1
print(isPalindrome)'''


#LONGEST WORD IN A SENTENCE
'''sentence = "python makes problem solving fun"
words = sentence.split()
longest = ""
for i in words:
    if len(i)>len(longest):
        longest=i
print(longest)
'''



'''Question: A=[1,2,3,2] target=3 count =2'''
# nums = [1,2,3,2]
# target = 5
# count = 0
# for i in range(len(nums)):
#     total = 0
#     for j in range(i,len(nums)):
#         total += nums[j]
#         if total == target:
#             count+=1
# print(count)


nums=[2,7,11,15]
target = 9
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        #check if sum matches the target
        if nums[i]+nums[j]==target:
            print(nums[i],nums[j])





nums=[2,7,11,15]
target = 9
left =0
right = len(nums)-1
while left<right:
    current_sum = nums[left]+nums[right]
    if current_sum==target:
        print(nums[left],nums[right])
        break
    elif current_sum<target:
        left+=1
    else:
        right-=1