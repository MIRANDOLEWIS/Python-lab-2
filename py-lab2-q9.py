qus_1 = tuple((input("enter your name : ")))

qus_2 = input("enter a letter of your name : ")

if qus_2 in qus_1:
    result = qus_1.index(qus_2)
    print("the index value of ",qus_2," of your name is :",result)

else :
    print("index value not found")    