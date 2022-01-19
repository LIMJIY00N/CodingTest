import sys
n,k = map(int,sys.stdin.readline().split())
coin = []
for i in range(n):
    coin.append(int(sys.stdin.readline()))
count= 0

i=n-1

for i in range(n):
    if coin[n-i-1]<=k:
        num = k//coin[n-i-1]
        count +=num
        k -= coin[n-i-1]*(num)
print(count)
