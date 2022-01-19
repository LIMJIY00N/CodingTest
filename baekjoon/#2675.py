n = int(input())
for i in range(n):
    res = ""
    num, line = input().split()
    for j in range(len(line)):
        res+=line[j]*int(num)
    print(res)