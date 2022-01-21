import sys
from collections import deque
def bfs(home,x,y):
    visit = []
    q = deque([])
    q.append([x,y])
    #상하 좌우 이므로, 상하죄우 체크할 dx와 dy
    dx=[0,0,1,-1]
    dy =[1,-1,0,0]
    
    while q:
        node = q.popleft()
        x = node[0]
        y = node[1]
        #노드를 방문하지 않았다면 방문기록에 추가
        if node not in visit:
            visit.append(node)
            #4번 for문 돌려서 
            for i in range(4):
                cx = x+dx[i]
                cy = y+dy[i]
                #상하좌우 중, 집이 있는 땅이 있다면
                if [cx,cy] in home:
                    #q에 해당 땅을 추가하기
                    q.append([cx,cy])
    return visit
            
    
    

n = int(sys.stdin.readline())
arr = []
#입력받은 값으로 2차원 배열 만들기 
for i in range(n):
    line = sys.stdin.readline()
    tmp = []
    for j in range(n):
        tmp.append(int(line[j]))
    arr.append(tmp)

#집이 있는 땅을 home 리스트에 넣기
home = []
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            home.append([i,j])
#총 단지의 수
num_danji = 0
#한 단지에 있는 집의 갯수   
homes_in_danji = []
#순회 하지 않은 집이 있는 땅이 있다면,
while home:
    #순회하고
    res = bfs(home,home[0][0],home[0][1])
    #res 받아올 때마다 단지 수 더해주기
    num_danji+=1
    #res의 길이는 한 단지에 있는 갯수이므로 homes_in_danji에 추가
    homes_in_danji.append(len(res))
    
    for i in range(len(res)):
        if res[i] in home:
            #집이 있는 모든 땅이 담긴 home에서, 순회한 땅들은 빼주기
            home.pop(home.index(res[i]))
#단지갯수 출력
print(num_danji)
#오름차순으로 출력해야 하므로 정렬 후 출력 
homes_in_danji.sort()
print('\n'.join(map(str,homes_in_danji)))