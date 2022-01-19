'''
import sys
n = int(sys.stdin.readline())
arr = []
res = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
arr = sorted(arr,key = lambda x:(x[1],x[0]))
e = 0
for item in arr:
    if e<=item[0]:
        res.append(item)
        e = item[1]
print(len(res))
'''

n = int(input())
arr = []
res = []
for i in range(n):
    arr.append(list(map(int,input().split())))
#회의 소요시간, 회의 시작시간 순으로 정렬
arr = sorted(arr,key = lambda x:(x[1]-x[0],x[0]))
#회의를 진행할 수 있는 시간을 저장할 left 리스트 
left = [[0,2**31-1]]
idx = 0
for item in arr:
	#정렬한 배열에 대해
    if idx == 0:
    #결과 배열 res에 첫번째 원소 추가
        res.append(item)
        #만약 item이 [3,5]라면 [0,3], [5,~]시간에 회의를 진행할 수 있으므로 left를 다음과 같이 바꿈
        left.append([left[0][0],item[0]])
        left.append([item[1],left[0][1]])
        #[0,2**31,1]값 제거
        left.pop(0)
        #인덱스 늘려주기
        idx+=1
    #첫번째 원소가 아니라면    
    else:
        #시작시간은 item의 0번째, 종료시간은 item의 1번째 수
        s = item[0]
        e = item[1]
        idx+=1
        #left배열을 돌면서
        for i in range(len(left)): 
            
			#회의를 진행할 수 있는 시간이 있는지 살펴본다.
            #ex. item이 [3,5]이고 left가 [[1,6],[7,~]]이면, [3,5]는 [1,5]시간 내에 진행할 수 있으므로
            if s>=left[i][0] and e<=left[i][1]:
            #item의 회의를 진행할 수 있다 판단하고 res에 item을 추가한다.
                    res.append(item)
                    #[1,5] 시간 내에 진행할 수 있다면, [1,6]를 제거하고, [1,3],[5,6]을 left에 추가한다.
                    cal = left.pop(i)
                    if cal[0] !=item[0]:
                        left.append([cal[0],item[0]])
                    if item[1]!=cal[1]:
                        left.append([item[1],cal[1]])
                    break;
                    #left를 정렬한다.
                    left.sort()


print(len(res))
