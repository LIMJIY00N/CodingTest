from collections import deque
n,m=map(int,input().split())
nums=list(map(int,input().split()))

arr=deque([i+1 for i in range(n)])
gap=0
count=0
flag=0

for i in range(m):
    flag = 0
    if nums[i]==arr[0]:
        arr.popleft()   
        
    else:
        gap = arr.index(nums[i])
        if gap>len(arr)/2:
            gap = len(arr)-gap
            flag=1 
            
        if flag==0:
            for j in range(gap):
                arr.rotate(-1)
                #앞에서 뒤로
                
            arr.popleft()
            count+=gap
        
        elif flag==1:
            
            for j in range(gap):
                #뒤에서 앞으로
                arr.rotate(1)
            arr.popleft()
            count+=gap
        
print(count)
    

