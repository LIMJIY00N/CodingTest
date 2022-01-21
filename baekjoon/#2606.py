from sys import setrecursionlimit
import sys
setrecursionlimit(10**6)
from collections import deque
#bfs
def bfs(graph,start_node):
    visit = []
    q = deque([])
    q.append(start_node)
    while q:
        node = q.popleft()
        if node not in visit:
            visit.append(node)
            q.extend(graph[node])
    return visit
#dfs stack
def dfs(graph,start_node):
    visit = []
    stack = []
    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
            
    return visit
#dfs 재귀
def dfs_recur(graph,start_node,visit):
    visit.append(start_node)
    for node in graph[start_node]:
        if node not in visit:
            dfs_recur(graph,node,visit)
    return visit
            
            
all_com = int(sys.stdin.readline())
linked = int(sys.stdin.readline())
graph = [[] for i in range(all_com+1)]

for i in range(linked):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

#print(len(bfs(graph,1))-1)
#print(len(dfs(graph,1))-1)
print(len(dfs_recur(graph,1,[]))-1)
    