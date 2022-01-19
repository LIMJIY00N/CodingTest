
import sys
n = int(sys.stdin.readline())
road = list(map(int,sys.stdin.readline().split()))
city = list(map(int,sys.stdin.readline().split()))
res = 0
min_city = city[0]
for i in range(n-1):
    if city[i]<min_city:
        min_city = city[i]
    res+=min_city*road[i]
print(res)