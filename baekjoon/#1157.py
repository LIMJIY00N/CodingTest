s = input().upper()
dic = {s[i]:0 for i in range(len(s))}
for i in range(len(s)):
    if s[i] in dic:
        dic[s[i]]+=1

arr = sorted(dic.items(),key=lambda x:(x[1]))
if len(arr)>1:
    if arr[len(arr)-1][1]==arr[len(arr)-2][1]:
        print("?")
    else:
        print(arr[len(arr)-1][0])
else:
    print(arr[0][0])