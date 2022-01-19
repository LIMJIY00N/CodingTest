from itertools import combinations,permutations
import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
#조합으로 6명이면 3명씩, 4명이면 2명씩 뽑기    
combi =list(combinations([i for i in range(1,n+1)],int(n/2)))
combi_set = []
#combi에서 마지막 원소와 첫번째 원소는 각각 (1,2), (3,4) 등의 형식이므로 
#각각 link팀, start팀의 팀원이 됨
for i in range(int(len(combi)/2)):
    combi_set.append([combi[i], combi[len(combi)-i-1]])
#각 경우 당 link 팀의 점수 합
link_score = 0
#각 경우 당 start 팀의 점수 합
start_score=0
#두 팀의 점수 차를 저장하는 배열
score_gap = []

#combi_set은 [(1,2),(3,4)]와 같은 형식이므로 item은 [(1,2),(3,4)]
for item in combi_set:
    start_score = 0
    link_score = 0
    #각 팀당 순열을 구함 ex) 위의 예시에서 start팀은 1,2가 팀원이므로
    #arr[1][2]와 arr[2][1]을 더해야 하므로 (1,2),(2,1)의 순열을 구하여 
    #arr에서 점수를 가져와 더해준다.
    start_lst=list(permutations(item[0],2))
    link_lst =list(permutations(item[1],2))
    
    for i in range(len(start_lst)):
        start_score+=arr[start_lst[i][0]-1][start_lst[i][1]-1]
        link_score+=arr[link_lst[i][0]-1][link_lst[i][1]-1]
    #두 점수 차를 절댓값으로 구하여 score_gap에 append한다.
    score_gap.append(abs(start_score-link_score))
#두 점수 차의 최솟값을 출력한다.
print(min(score_gap))