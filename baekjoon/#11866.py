n,k=map(int,input().split())
arr =[i+1 for i in range(n)]
arr2=[]

i=0

while arr:
    idx = ((i+k-1)%len(arr))
    pop_num=arr.pop(idx)
    arr2.append(pop_num)
    i=idx
print('<',end='')
for i in range(n):
    if i!=n-1:
        print(arr2[i],end=', ')
    else:
        print(arr2[i],end='>')
