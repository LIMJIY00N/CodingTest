from collections import deque    
def bfs(x,y):
    queue = deque([])
    dx,dy = [-1,1,0,0],[0,0,-1,1] #방향 상하좌우 판단 위해
    #큐에 넣기
    queue.append([x,y])
    while queue:#초기 배추에서 인접한 배추의 인접한 배추까지 모두 찾기 
        x,y = queue.popleft()
        #상하좌우 인접한 배추 있는지 찾기
        for i in range(4):
            nx,ny = dx[i]+x, dy[i]+y
            if 0 <= nx < m and 0 <= ny < n:
                #인접한 배추가 있다면 0으로 만들고 큐에 넣기(해당 배추의 인접한 배추 또 찾아야하므로)
                if flag[nx][ny]==1:
                    flag[nx][ny] = 0 
                    queue.append([nx,ny])



T = int(input())

for i in range(T):
    count=0
    m,n,k = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(k)] #좌표 입력받기
    flag = []
    #모두 0으로 채워져있는 이중리스트 flag 만들기
    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append(0)
        flag.append(tmp)
    
    #배추가 있는 좌표의  flag값을 1로 만들기
    for item in arr:
        flag[item[0]][item[1]]=1
        #원래 여기서 bfs를 돌렸는데 flag의 초기 1을 모두 설정한 후에 해주어야 했다. 
        #모두 1로 설정된 후에 하면 bfs 수행 결과가 반환되므로 모두 1로 설정 후에 bfs를 수행해야 한다.
        #bfs(item[0],item[1])
        #count+=1
    count = 0
    for i in range(m): 
        for j in range(n): 
            #배추가 심어져 있다면
            if flag[i][j]==1:
                #print("i,j:",end=' ')
                #print(i,j)
                #bfs를 수행하여 인접한 배추의 인접한 배추까지 모두 찾고 count 1더하기
                bfs(i,j)
                count+=1
    
    print(count)
    


            

