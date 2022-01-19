x=[]
y=[]
for i in range(3):
    a,b = input().split()
    x.append(a)
    y.append(b)
x=sorted(list(map(int,x)))
y=sorted(list(map(int,y)))
if x[1]-x[0]==0:
    res_x=x[2]
elif x[2]-x[1]==0:
    res_x=x[0]
if y[1]-y[0]==0:
    res_y=y[2]
elif y[2]-y[1]==0:
    res_y=y[0]
print(res_x, res_y)