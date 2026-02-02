''''ques: validate the mobile number by using regex pattern '''
# import re
# mobile="8690129384"
# #pattern=r"^/d{10}$"
# pattern=r"^[0-9]{10}$"  #we have to use r everytime for regix pattern
# if re.match(pattern,mobile):
#     print("valid mobile number")
# else:
#     print("Invalid mobile number")

'''ques: test@gmail.com and admin@yahoo.in (you have extract all the  details of the ) extract email from a string'''
# import re
# text="COntact us at test@gmail.com or admin@yahoo.in"
# pattern=r"[\w.-]+@[\w.-]+\.\w+"
# emails=re.findall(pattern,text)
# print(emails)

'''Ques: order123 price123 quantity6'''
# text="order123 price123 quantity6"
# p=r""

'''Ques: Validate a strong password
-at least 8 characters
-one uppercase
-one lowercase 
-one digit
--one special character'''

# text="password"
# p=r"^(?=.*[a-z]) (?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}"


# '''PAN Card validation code'''
# import re
# text = "ABCDE1234F"
# pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]$"
# if re.match(pattern, text):
#     print("Valid PAN number")
# else:
#     print("Invalid PAN number")


#ipv4
import re
ipv4 = "185.107.106.772"
p = r"^([0-9]{1,3}\.){3}[0-9]{1,3}$"
if re.match(p, ipv4):
    print("Valid IPv4 format")
else:
    print("Invalid IPv4 format")                                                                                  