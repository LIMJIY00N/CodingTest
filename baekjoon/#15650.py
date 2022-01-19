from itertools import combinations
N,M = map(int,input().split())
arr = [i+1 for i in range(N)]
for item in list(combinations(arr,M)):
    print(*item)
