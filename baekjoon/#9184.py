import sys
d_abc = [[[0]*21 for i in range(21)] for i in range(21)] 

def w(a,b,c):

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        if d_abc[20][20][20] ==0:
            d_abc[20][20][20] = w(20,20,20)
        return d_abc[20][20][20] 
    
    
    
    if a < b and b < c:
        if d_abc[a][b][c] ==0:        
            d_abc[a][b][c] = w(a,b,c-1)+w(a,b-1,c-1)-w(a, b-1, c)
        return d_abc[a][b][c]
        

    else:
        if d_abc[a][b][c] ==0:
            d_abc[a][b][c] = w(a-1, b, c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
        return d_abc[a][b][c]

while True:
    a,b,c = map(int,sys.stdin.readline().split())
    if a==-1 and b==-1 and c== -1:
        break
    else:
        print("w({}, {}, {}) = {}".format(a,b,c,w(a,b,c)))
        