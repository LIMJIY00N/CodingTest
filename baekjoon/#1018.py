import math
import sys
n,m = map(int,sys.stdin.readline().split())
arr = [sys.stdin.readline() for i in range(n)]
down_many = n-8+1
left_many = m-8+1



count =[];
for i in range(down_many):
    for j in range(left_many):
        cnt_odd=[0,0]
        cnt_even=[0,0]
        

        for k in range(i,i+8):
            for l in range(j,j+8):
                
                if (k+l)%2==0:
                 
                    if arr[k][l] == 'B':
                        
                        cnt_even[0]+=1
                    if arr[k][l] == 'W':
                     
                        cnt_even[1]+=1
                   
                #홀수번째            
                if(k+l)%2==1:
                   
                    if arr[k][l] =='B':
                        #print(arr[k][l])
                        cnt_odd[0]+=1
                    if arr[k][l] =='W':
                        #print(arr[k][l])
                        cnt_odd[1]+=1
      
        mx = max(max(cnt_odd),max(cnt_even))
        if mx in cnt_odd:
            idx=cnt_odd.index(mx)
            count.append(32-cnt_odd[idx]+32-cnt_even[1-idx])
        elif mx in cnt_even:
            idx = cnt_even.index(mx)
            count.append(32-cnt_even[idx]+32-cnt_odd[1-idx])
print(min(count))
        
        
               
                    
                
                

        
    

