n,m = input().split()
rev_n =""
rev_m =""
for i in range(3):
    rev_n+=n[2-i]
    rev_m+=m[2-i]
    
if int(rev_n)>int(rev_m):
    print(rev_n)
else:
    print(rev_m)
    