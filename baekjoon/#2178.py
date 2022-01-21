import sys
from collections import deque
def bfs(arr,x,y):   
    dx = [1,-1,0,0]
    dy = [0,0,-1,1] 
    
    q = deque([])
    visit = []
    
    q.append([x,y])        
    while q:
        node = q.popleft()
        x = node[0]
        y = node[1]
        if x ==n-1 and y==m-1:
            return arr[x][y]
        
        if [x,y] not in visit:
            visit.append(node) 
            for i in range(4):
                cx = dx[i]+x
                cy = dy[i]+y
                if 0<=cx<n and 0<=cy<m and arr[cx][cy]==1:           
                    q.append([cx,cy])
                    arr[cx][cy] = arr[x][y]+1
                
n,m = map(int,sys.stdin.readline().split())
arr = []
for i in range(n):
    line = sys.stdin.readline()
    tmp = []
    for j in range(m):
        tmp.append(int(line[j]))
    arr.append(tmp)

print(bfs(arr,0,0))