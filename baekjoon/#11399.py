n = int(input())
P = sorted(map(int,input().split()))

sum = 0
for i in range(n):
    sum += P[i]*(n-i)
    
print(sum)