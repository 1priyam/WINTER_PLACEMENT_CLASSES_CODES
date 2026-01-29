'''try:
    #risky code
except:
    #error handling code'''


'''try:
    a=int(input("Enter first number:"))
    b= int(input("Enter second number:"))
    print(a/b)

except:
    print("errror occurredd!!!!!!!!!!!!!!!!!")
'''



try:
    file = open("movies.txt","r")
    print(file.read())
except FileNotFoundError:
    print("file not found")
finally:
    print("program ends")                            #finally is the code which evertime you runthe code it will run everytime