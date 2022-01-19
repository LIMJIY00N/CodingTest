import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    comm = sys.stdin.readline().strip()
    
    if "push" in comm:
        
        c,num = comm.split()
        
        arr.append(int(num))
        
    elif comm=="top":
        if arr:
            print(arr[-1])
            
        else:
            print(-1)
    
    elif comm=="pop":
        if arr:
            print(arr.pop())
        else:
            print(-1)    
        
    elif comm=="empty":
        if arr:
            print(0)
        else:
            print(1)
    elif comm =="size":
       print(len(arr)) 