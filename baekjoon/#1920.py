import sys
n=int(sys.stdin.readline())
arr_n = list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
arr_m = list(map(int,sys.stdin.readline().split()))
arr_n.sort()

for i in range(m):
    left = 0
    right = len(arr_n)-1
    while left<=right:
        mid = (left+right)//2
        if arr_m[i] == arr_n[mid]:
            print(1)
            break
        elif arr_m[i]<arr_n[mid]:
            right = mid-1
        else:
            left = mid+1
    if left>right:
        print(0)
