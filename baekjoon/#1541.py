from collections import deque
# '-' 기준으로 split하기
line = input().split('-')
#결과값 저장 변수
res = 0
#line은 첫번째 원소만 +하고, 나머지 원소들은 -를 기준으로 나눴기 때문에 
#그 합을 뺴주어야 한다.
for i in range(len(line)):
    #'+' 기준으로 다시 나눠서 int 를 담은 리스트 형식으로 바꾸기 
    lst = list(map(int,str(line[i]).split('+')))
    if i==0:
        #첫번째 원소면 합을 더해주고
        res+=sum(lst)
    else:
        #첫번째가 아니면 함을 빼주기
        res-=sum(lst)
print(res)
        