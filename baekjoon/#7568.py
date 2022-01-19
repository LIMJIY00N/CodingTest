n = int(input())
res = [1]*n
arr = [list(map(int,input().split())) for i in range(n)]
for i in range(len(arr)):
    for j in range(len(arr)):

        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
    
            res[i]+=1
print(" ".join(map(str,res)))