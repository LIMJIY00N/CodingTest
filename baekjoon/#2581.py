def check(num):
    if num==1:
        return False;
    for i in range(2,num):
        if num==2:
            return True
        if num!=2:
            if num%i==0:
                return False
        
    return True

m=int(input())
n=int(input())
arr=[]
for item in range(m,n+1):
    if(check(item)):
        arr.append(item)
if arr:
    print(sum(arr)) 
    print(arr[0])
else:
    print(-1)