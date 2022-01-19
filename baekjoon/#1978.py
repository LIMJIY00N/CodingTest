import sys    
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
cnt=0
for i in arr:
    if i==1:
        continue
    if i==2:
        cnt+=1
        continue
    for j in range(2,i):
        if i!=2 and i%j==0:
            break;
    
    if j == i-1:
        cnt+=1
print(cnt)
            
    
