def d(n):
    num =str(n)
    sum=n
    for i in num:
        sum+=int(i)
    return sum

arr={i:0 for i in range(1,10001)}

for i in range(1,10000):
    arr[d(i)]=-1
for key in arr:
    if arr[key]!=-1:
        print(key)