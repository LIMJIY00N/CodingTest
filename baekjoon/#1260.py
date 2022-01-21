import sys
from collections import deque
def bfs(graph,start_node):
    visit = []
    q =deque([])
    #큐에 첫 시작 노드를 넣는다.
    q.append(start_node)
    #q에 원소가 있는 동안에
    while q:
        #큐의 첫번째 원소를 뽑아온다.
        node = q.popleft()
        #뽑아온 노드를 처음 방문한다면
        if node not in visit:
            #방문 기록에 해당 노드를 추가한다. 
            visit.append(node)
            # 자식 노드들을 큐에 넣는다. 
            # 위에서 큐에서 popleft를 하므로, 방금 추가한 자식 노드들은 나중에 고려되고,
            # q의 앞부분은 node의 형제노드들이 있으므로 node의 형제 노드를 먼저 고려한다. 
            q.extend(graph[node])
    return visit

#스택을 활용하여 풀면 본 문제에서 원하는 순서로 나오지 않을 수 있으므로
#재귀를 사용했다.
def dfs(graph,start_node,visit):
    #방문 기록에 start_node 추가
    visit.append(start_node)
    #start_node의 자식 노드들에 대해서
    for node in graph[start_node]:
        #해당 자식 노드를 처음 방문 한다면
        if node not in visit:
            #해당 자식 노드의 자식 노드들에 대해 탐색한다.
            dfs(graph,node,visit)
    return visit

'''
#스택 사용
def dfs(graph, start_node):
    visit = []
    stack = []
    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return visit
'''
n,m,v = map(int,sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n): 
    graph[i+1].sort()
    
print(' '.join(map(str,dfs(graph,v,[]))))
print(' '.join(map(str,bfs(graph,v))))

