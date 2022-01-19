from itertools import permutations
N,M = map(int,input().split())
arr = list(permutations([i for i in range(1,N+1)],M))
for item in arr:
    print(*item)
