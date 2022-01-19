import sys
arr = []
for i in range(int(sys.stdin.readline())):
    arr.append(list(map(int,sys.stdin.readline().split(' '))))

arr.sort(key = lambda x:(x[1],x[0]))
for i in range(len(arr)):
    print(' '.join(map(str,arr[i])))
