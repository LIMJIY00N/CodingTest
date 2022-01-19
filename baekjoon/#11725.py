import sys
sys.setrecursionlimit(100000) #런타임 에러 방지

def dfs(curr,tree,parents):
    for item in tree[curr]:
        if parents[item] == 0:
            parents[item] = curr
            dfs(item,tree,parents)
    
    

n = int(sys.stdin.readline())
tree = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

res = {i:0 for i in range(1,n+1)}
#print(res)

dfs(1,tree,res)
for i in range(2,n+1):
    print(res[i])


'''
import sys
n = int(sys.stdin.readline())
tree = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
#print(tree)
res = {}
p = [1]
checked = [False]*(n+1)
#print(checked)
while p:
    parent = p.pop(0)
    checked[parent] = True
    for item in tree[parent]:
        if not checked[item]:
            checked[item] = True
            res[item] = parent
            p.append(item)
        #    print(res)

for i in range(2,n+1):
    print(res[i])
            

'''