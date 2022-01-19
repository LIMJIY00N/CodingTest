import sys
n=int(sys.stdin.readline())
arr_n = list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())

#이 알고리즘은 arr_n을 차례로 순회하여 arr_m에 있는지 체크하는 알고리즘이다.

#출력 시 처음 인덱스들의 순서 알기 위해 tmp로 받고
tmp = list(map(int,sys.stdin.readline().split()))
#효율적인 이진 탐색을 위해 중복 제거, 정렬한다
arr_m = sorted(set(tmp))

dic = {arr_m[i]:0 for i in range(len(arr_m))}


for i in range(n):
    left = 0
    right = len(arr_m)-1
    #right가 left보다 큰 동안
    while left<=right:
        #중앙값을 구한다
        mid = (left+right)//2
        #arr_m의 중앙값과 arr_n의 i번째 수가 같다면
        if arr_m[mid]==arr_n[i]:
            #딕셔너리의 해당 키의 값을 1 더하고 break한다
            dic[arr_m[mid]]+=1
            break
        #중앙값이 더 크다면 right를 mid-1로 조정 
        elif arr_m[mid]>arr_n[i]:
            right = mid-1
        #중앙값보다 arr_n[i]값이 더 크다면 left를 mid+1로 조정
        else:
            left = mid+1
#처음 들어온 값 [10 0 -5 2 3 4 5 -10]의 순서에 따라 dic에서 출력 
for i in range(m):
    if i!=m-1:
        print(dic[tmp[i]],end=' ')
    else:
        print(dic[tmp[i]])
        