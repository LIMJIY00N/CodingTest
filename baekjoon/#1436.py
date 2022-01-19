n = int(input())
num = 666
i=0
arr = [0]*10001

while(True):
    if i==n:
        print(arr[i])
        break;

    if "666" in str(num):
        i+=1
        arr[i]=num
    num+=1
