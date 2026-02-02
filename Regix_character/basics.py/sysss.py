# import sys
# print(sys.version)
# print(sys.platform)
# print(sys.argv)

import random
i=0
while i !=5 :
    i = int(input("Enter your winning: "))
    li =["stone", "Paper","scissor"]
    out=random.choice(li)
    print(out)
print("Congratulations you won Your Teaa!!!!")
