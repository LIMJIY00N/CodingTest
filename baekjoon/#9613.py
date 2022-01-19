import math
N = int(input())
for i in range(N):
    a,*arr = map(int,input().split())
    sum = 0
    for j in range(a):
        for k in range(j+1,a):
            sum+=math.gcd(arr[j],arr[k])
    print(sum)