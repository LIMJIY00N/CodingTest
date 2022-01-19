import sys    
n=int(sys.stdin.readline())
arr=[int(sys.stdin.readline()) for i in range(n)]
stack=[]
res=[]
num=1
flag=0
i=0

while True:
    
    if not stack:
        stack.append(num)
        res.append('+')
        num+=1
   
    if stack[-1]==arr[i]:
        stack.pop()
        res.append('-')
        i+=1
    
    else:    
        stack.append(num)
        res.append('+')
        num+=1
   
    if not stack and num>n:
        break;
    
    if arr and num>n and stack[-1]>arr[i]:
        print("NO")
        flag=1
        break;
if flag==0:
    for item in res:
        print(item)