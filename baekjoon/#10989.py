import sys
n = int(sys.stdin.readline())
lst = [0]*10000
for i in range(n):
    lst[int(sys.stdin.readline())-1]+=1
for i in range (len(lst)):
    if lst[i]!=0:
        for j in range(lst[i]):
            print(i+1)