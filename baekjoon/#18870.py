import sys
from typing import List
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
#결과 저장 리스트
res = [0]*n
lst = []


#arr을 집합화하고 내림차순 정렬
set_arr = sorted(set(arr))
dic = {set_arr[i]:i for i in range(len(set_arr))}
print(" ".join(map(str,[dic[item] for item in arr])))




