dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

dic4 = {}

for x in (dic1,dic2,dic3):
    dic4.update(x)

print("the  concatenate of dictionaries are \n",str(dic4))    