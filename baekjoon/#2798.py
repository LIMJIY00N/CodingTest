import sys
from itertools import combinations

n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
lst = [item for item in combinations(arr,3) if sum(item)<=m]

dic = {sum(item)-m:item for item in lst}

print(sum(dic[max(dic)]))
        