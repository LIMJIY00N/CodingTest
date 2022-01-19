n = int(input())

for i in range(n):
    stack = []
    line = input()
    for item in line:
        if stack:
            if item =='(':
            
                stack.append(item)
                
            elif item==')':
                if stack[-1]=='(':
                    stack.pop()
                    
                else:
                    stack.append(item)
                
        else:
            stack.append(item)

    if stack:
        print("NO")
    else:
        print("YES")