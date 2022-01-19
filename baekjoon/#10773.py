import sys
k = int(sys.stdin.readline())
arr = []
for i in range(k):
    num = int(input())
    if num==0:
        n = arr.pop()
        
    else:
        arr.append(num)
print(sum(arr))        