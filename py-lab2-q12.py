#method 1
a = ['m','a','s','h','u','p']

b = "".join(a)

print(b)
print(type(b))

#method 2
a = ['m','a','s','h','u','p']

b = ""

for x in a:
    b = b + x

print(b)
print(type(b))    