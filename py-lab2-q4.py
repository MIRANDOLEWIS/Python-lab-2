from collections import Counter

user = input("Enter any words: ")

user_len = Counter(user)

for x,y in user_len.items():

    if y > 1:
        
        print("{0} repeat at {1} times".format(x,y))

