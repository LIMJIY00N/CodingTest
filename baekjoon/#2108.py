import sys

n = int(sys.stdin.readline())
arr = []
idx = {}
#숫자 받아서 arr 리스트에 넣기 
for i in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)
    #idx에 입력받은 숫자가 키로 없으면 해당 숫자를 키로하여 값을 1로 세팅
    if num not in idx:
        idx[num] = 1
    #입력받은 숫자가 idx에 키로 있으면, 하나가 더 들어온 것이므로 값을 1 더해줌
    elif num in idx:
        idx[num]+=1
#갯수 1개일 때를 따로 빼기 
if n==1:
    print(arr[0])
    print(arr[0])
    print(arr[0])
    print(0)
#갯수가 1개 이상이면
else:
    #우선 오름차순 정렬
    arr.sort()
    #산술평균        
    avg = int(round(sum(arr)/n))
    print(avg)
    #중앙값은 오름차순 정렬한 것에서 가운데 값
    mid = arr[int(n/2)]
    print(mid)
    #최빈값
    #sorted 하면 리스트 반환. 원소는 튜플 
    #빈도수 내림차순(큰->작은), 키값 오름차순(작은->큰)
    idx = sorted(idx.items(),key = lambda x:(-x[1],x[0]))
    idx =[idx[0],idx[1]]
    if idx[0][1] == idx[1][1]:
        print(idx[1][0])
    else:
        print(idx[0][0])
    
    # for i in range(1,len(idx)):
    #     if idx[0][1] == idx[i][1]:
    #         print(idx[1][0])
    #         break;
    #     else:
    #         print("here")
    #         print(idx[0][0])
    #         break;

    #범위
    ran = arr[n-1] - arr[0]
    print(ran)  
    