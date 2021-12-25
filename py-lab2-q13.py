
a = [1,2,3,4,5,6,7,8]

b = [[]]

for i in range (len(a)+1):
    for j in range(i):

        b.append(a[j:i])
 

print(b)