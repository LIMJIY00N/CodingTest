n=int(input())
for i in range(n):
    if i!=0:
        print()
    for j in range(n-i-1):
        
        print(" ",end='')
    for j in range(n-i-1,n):
        print("*",end="")