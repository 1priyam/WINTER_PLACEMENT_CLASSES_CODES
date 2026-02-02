import re
#1.dot(.)
# text="cat cot cut c@t"
# result=re.findall("c.t",text)
# print(result)

#2.start of a string(^)
# text="Hello World"
# print(bool(re.search("^Hello",text)))
# print(bool(re.search("^World",text)))

#3.ending of string($)
# text="Hello World"
# print(bool(re.search("Hello$",text)))
# print(bool(re.search("World$",text)))

# 4. 0 or more (*)
# text="helloooo"
# result=re.findall("lo*",text)
# print(result)

#5.one or more(+)
# text="helloooo"
# result=re.findall("lo+",text)
# print(result)

#6.0 or 1 time (?)
# text="color colour"
# result=re.findall("colou?r",text)
# print(result)

#7.character set([])
# text="apple ball cat"
# result=re.findall("[abc]",text)
# print(result)

#8.Digits([0-9])
# text = "My age is 30"
# result=re.findall("[0-9]",text)
# print(result)

#12 digits (\d)
# text="Marks: 90"
# result=re.findall("\d",text)
# print(result)

#13. non digits(\D)
# text="Marks: 90"
# result=re.findall("\D",text)
# print(result)

#14. words (\w)
# text="Marks: 90"
# result=re.findall("\w",text)
# print(result)

#15. not words(\W)
# text="Marks: 90"
# result=re.findall("\W",text)
# print(result)

#16. space (\s)
# text="Marks: 90"
# result=re.findall("\s",text)
# print(result)

#17. No space(\S)
# text="Marks: 90"
# result=re.findall("\S",text)
# print(result)

#18. repetition count({})
# text="Phone: 8739391923"
# result=re.findall("\d{10}",text)
# print(result)

#19.or operator(|)
# text = "I have a cat and a dog"
# result=re.findall("cat|dog",text)
# print(result)

#20.grouping (())
text = "abab ab"
result=re.findall("(ab)+",text)
print(result)
