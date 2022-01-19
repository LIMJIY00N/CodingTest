import math
num=str(math.factorial(int(input())))

for i in range(len(num)):
    if num[len(num)-i-1]!='0':
        idx=len(num)-i-1
        break
        
print(len(num)-idx-1)
