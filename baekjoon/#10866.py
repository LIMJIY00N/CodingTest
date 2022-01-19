import sys
from collections import deque
deq=deque()
n=int(sys.stdin.readline())
for i in range(n):
    line=sys.stdin.readline().strip()
    if "push_front" in line:
        _,num=line.split()
        deq.appendleft(int(num))
    elif "push_back" in line:
        _,num=line.split()
        deq.append(int(num))
    elif line=="front":
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif line=="size":
        print(len(deq))
    elif line=="empty":
        if deq:
            print(0)
        else:
            print(1)
    elif line=="back":
        if deq:
            print(deq[-1])
        else:
            print(-1)
    elif line=="pop_front":
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif line=="pop_back":
        if deq:
            print(deq.pop())
        else:
            print(-1)