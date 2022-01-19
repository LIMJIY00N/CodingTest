arr = []
for i in range(int(input())):
    s = input()
    if s not in arr:
        arr.append(s) 
length = [len(item) for item in arr]
pairs = zip(arr,length)
lst  = []
lst = list(map(list,pairs))
lst.sort(key = lambda x:(x[1],x[0]))
for item in lst:
    print(item[0])