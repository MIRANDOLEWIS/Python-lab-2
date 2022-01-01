import random

upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_letter = upper_letter.lower()
symbols = "!@#$%^&*()[]_-+=<>,.?/\\;:"
dig = "0123456789"

upper,lower,symb,nums = True,True,True,True

paswrd = ""

if upper:
    paswrd += upper_letter

if lower:
    paswrd += lower_letter

if symb:
   paswrd +=  symbols

if nums:
    paswrd += dig     

length = 20

for x in range(0,1):
    password = "".join(random.sample(paswrd,length))

    print("your new password is ", password)
