import math
n,k=[int(x) for x in input().split()]
res=1
for i in range(n-k+1,n+1):
    res*=i
    
print(int(res/math.factorial(k)))