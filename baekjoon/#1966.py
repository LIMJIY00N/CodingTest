from collections import deque
for i in range(int(input())):
    n,m=map(int,input().split())
    imp=deque(map(int,input().split()))
    
    count=0 
    
    while True:
        if imp[0]==max(imp):
            if m==0:
                print(count+1)
                break
            else:
                imp.popleft()
                count+=1
                m=(len(imp)+m-1)%len(imp)

        
        else:
            imp.rotate(-1)
            m=(len(imp)+m-1)%len(imp) 
            
                 
        
        
    