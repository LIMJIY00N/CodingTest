def fac(res,n):

    if n>0:
        res*=n
        fac(res,n-1)
    else:
        
        print(res)

fac(1,int(input()))
