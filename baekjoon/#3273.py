import sys
n = int(sys.stdin.readline())
arr = sorted(map(int,(input().split())))
x = int(sys.stdin.readline())

end = n-1
count = 0

for start in range(len(arr)):
    while end>start:
        if arr[start]+arr[end]>x:
            end-=1
        elif arr[start]+arr[end]==x:
            count+=1
            end = n-1
            break
        else:
            break
print(count)