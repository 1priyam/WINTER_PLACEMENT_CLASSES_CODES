'''===================================module project1============================================================
- in this we will use
* maths
* random
* counter
1. Generate random number
2. check which number
3. round numbers using maths
4. count how many timees number appear
5.saves the result in a file
'''



# name1="priyam"
# name2="tiwari"
# fullname=name2.join(name1)
# print(fullname)

# 5. saves the result in a file 
'''import random
import math
import os
import re
from collections import Counter
numbers = [random.randint(1,10) for _ in range(10)]
#even or oddd
even_numbers=[]
odd_numbers=[]
for num in numbers:
    num_str=str(num)
    if re.search(r"^[02468]$", num_str):
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
#calcualting average
average = sum(numbers)/len(numbers)
#round off the average 
rounded_avg=math.ceil(average)
#count number
count_numbers=Counter(numbers)
#save result using os 
if not os.path.exists("easy_reports"):
    os.mkdir("easy_reports")

#file paths
file_path = os.path.join("easy_reports","number_report.txt")

#write data to a file
file=open(file_path,"w")
file.write(f"Genereated Numbers:{numbers}")
file.write(f"Generated number: {even_numbers}")
file.write(f"odd_number: {odd_numbers}")
file.write(f"average:{rounded_avg}")
file.write(f"number count:\n")

for num, count in count_numbers.items():
    file.write(f"{num} :{count}\n")

file.close()
print(numbers)
print(odd_numbers)
print(even_numbers)
print(rounded_avg)
print(count_numbers)
print(file_path)
'''




# 1.generate random password
# 2. check password strength
# 3.count character used in password
# 4.gives a strengh score using math
# 5. saves the result in a file using os
import random      #----------------------> importing random
import math        #----------------------> importing math
import os          #----------------------> importing os
import re
from collections import Counter

#---------------------- Generate random password ----------------------
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$"
pass_length = 8
password = "".join(random.choice(chars) for _ in range(pass_length))

print("Password:", password)

#---------------------- Check password strength ----------------------
upper = len(re.findall(r"[A-Z]", password))
lower = len(re.findall(r"[a-z]", password))
digit = len(re.findall(r"[0-9]", password))
special = len(re.findall(r"[@#$]", password))

#---------------------- Count characters ----------------------
char_count = Counter(password)

#---------------------- Strength score using math ----------------------
score = upper + lower + digit + (special * 2)
strength_score = math.ceil(score / pass_length)

if strength_score <= 2:
    strength = "Weak"# Password is weak if score is very low
elif strength_score <= 4:
    strength = "Medium"# Password is medium if score is average
else:
    strength = "Strong"# Password is Strong if score is high

#---------------------- Save result using os ----------------------
if not os.path.exists("password_reports"):
    os.mkdir("password_reports")

file_path = os.path.join("password_reports", "password_report.txt")

file = open(file_path, "w") # Opens the file in write mode
file.write(f"Password: {password}\n")# Writes password to the file
file.write(f"Uppercase Letters: {upper}\n")#upercase count
file.write(f"Lowercase Letters: {lower}\n")#lowercase count
file.write(f"Digits: {digit}\n")#number count
file.write(f"Special Characters: {special}\n")#special count
file.write(f"Strength Score: {strength_score}\n")#strenght score
file.write(f"Password Strength: {strength}\n")#final strenght result
file.write("Character Count:\n")

for ch, count in char_count.items():
    file.write(f"{ch} : {count}\n") #it will  write each character and its count

file.close()

#---------------------- Output ----------------------
print(strength)
print(strength_score)
print(char_count)
print(file_path)