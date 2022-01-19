dict = {chr(c) :-1 for c in range(ord('a'),ord('z')+1)}
line = input()
for i in range(len(line)): 
    dict[line[len(line)-i-1]] = len(line)-i-1


    
res_arr = []
res_arr = [value for key,value in dict.items()]


print(" ".join(map(str,res_arr)))
