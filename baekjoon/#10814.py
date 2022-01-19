arr = []
for i in range(int(input())):
    tmp = []
    age,name = input().split()
    tmp.append(int(age))
    tmp.append(name)
    tmp.append(i)
   
    arr.append(tmp)


arr.sort(key = lambda x:(x[0],x[2]))
for item in arr:
    print(str(item[0])+' '+item[1])

