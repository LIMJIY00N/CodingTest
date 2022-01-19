n = int(input())
for i in range(n):
    str = input()
    for j in range(len(str)-1):
        if str[j] != str[j+1]:
            if str[j] in str[j+1:]:
                n-=1
                break;
print(n)