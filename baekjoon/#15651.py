from itertools import product
n,m = map(int,input().split())
a = product(range(1,n+1),repeat = m)

for i in a:
    print(*i)