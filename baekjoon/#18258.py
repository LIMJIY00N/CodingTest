import sys
from collections import deque 
n=int(sys.stdin.readline())
queue=deque()
for i in range(n):
    line = sys.stdin.readline().strip()
    if "push" in line:
        a,num=line.split()
        queue.append(num)
    elif line=="pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif line=="size":
        print(len(queue))
    elif line=="front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif line=="back":
        if queue:
            print(queue[-1])
        else:
            print(-1) 
    elif line=="empty":
        if queue:
            print(0)
        else:
            print(1)
        
        