import sys
from collections import deque
def bfs(graph,start_node,len_pan,dest):
    visit = [[False for i in range(len_pan)] for _ in range(len_pan)]
    #원래는 visit에 [1,2]과 같은 좌표를 append하는 방법을 사용하였음
    #따라서 visit은 초기에 빈 리스트였음
    q = deque([])
    q.append(start_node)
    #q.append([start_node[0],start_node[1],0])
    dx = [-2,-1,1,2,-2,-1,1,2]
    dy = [1,2,2,1,-1,-2,-2,-1]
    
    while q:
        node = q.popleft()
        #print(q)
        x = node[0]
        y = node[1]
        if x == dest[0] and y==dest[1]:
                #return node[2]
                return graph[x][y]
        #위와 같이 visit을 선언하니, 
        #if [x,y] in visit: 과 같은 코드를 사용했고, in이 시간복잡도가 높아 
        #나오는 시간초과 문제였음
        #또한, 정답 제출에는 문제가 없지만 주석처리한 코드와 같이 q에 아예 횟수를 추가해주니
        #600ms정도 덜 걸렸음
        if not visit[x][y]:
            visit[x][y] = True
            for i in range(8):
                cx = dx[i]+x
                cy = dy[i]+y
                if 0<=cx<len_pan and 0<=cy<len_pan :
                    #q.append([cx,cy,node[2]+1])
                    graph[cx][cy] = graph[x][y]+1
                    q.append([cx,cy])

        

for _ in range(int(sys.stdin.readline())):
    len_pan =int(sys.stdin.readline())
    curr = list(map(int,sys.stdin.readline().split()))
    dest = list(map(int,sys.stdin.readline().split()))
    graph = [[0 for i in range(len_pan)] for _ in range(len_pan)] 
    print(bfs(graph,curr,len_pan,dest))