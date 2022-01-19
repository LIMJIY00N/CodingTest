from collections import deque
import sys
T = int(sys.stdin.readline())
for i in range(T):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    line=sys.stdin.readline().strip()
    if len(line)!=2:
        arr = deque(map(int,line[1:-1].split(',')))
    else:
        arr=[]
    flag=0
    isError=0
    for item in p:
        if item=='R':
            flag= abs(flag-1)
            
        elif item=='D':
            if arr:
                if flag==1: #reverse 모드 
                    arr.pop()

                if flag==0:
                    arr.popleft()
            else:
                isError=1
                print('error')
                break
    if isError==0:
        if flag==1:
            arr.reverse()
        print('['+','.join(map(str,list(arr)))+']')
        
                
                