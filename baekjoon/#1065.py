def check(num):
    n = str(num)
    arr =[]
    flag=0
    for i in range(len(n)-1):
        if len(arr)==0:
            arr.append(int(n[i+1])-int(n[i]))
        else:
            if arr[0]!=int(n[i+1])-int(n[i]):
                flag=1
                return False
            
    if flag==0:
        return True
    
n = int(input())
sum=0
for i in range(1,n+1):
    if check(i):
        sum+=1
print(sum)