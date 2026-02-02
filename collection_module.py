'''from collections import Counter
fruits = ["Banana", "orange","Mango","Mango","apple","Banana"]
count = Counter(fruits)
print(count)

text = "Hello"
cnt = Counter(text)
print(cnt)

sentence = "python is easy and python is powerful"
ctt=Counter(sentence.split())
print(ctt) '''

import os 
# current_path = os.getcwd()
# print(current_path)

folder_name = "my_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("folder created successfully")

else:
    print("folder is already present")

