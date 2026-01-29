'''s = "python PRoGramMing"
print(len(s))
print(s[-1])
print(s[:4])
print(s[7:18])
print(s.lower())
print(s.upper())
k = "           python ProgrMMIng   "  
print(k.strip())

print(s.replace("python","java"))
print(s.find("o"))

word=s.split()
print(word)

a = "abc"
print(a.isalpha())
print(a.isdigit())
b="123"
print(b.isdigit())
print(s.count("p"))
print(s)
print(s.startswith("py"))
print(s.endswith("ing"))
'''

                    #--------------------------------------------------------------------------------------------------#

s = "apple"
for ch in s:
    print(ch,":",s.count(ch))




s = "pyhton"
result=""
for ch in s:
    if ch in "aeiou":
        result+="*"
    else:
        result+=ch
print(result)



























