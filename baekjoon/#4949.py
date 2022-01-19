while True:
    
    line = input()
    stack = []
    if line=='.':
        break;
    flag =0
    for item in line:
        if item =='(':
            stack.append(item)
            
        elif item ==')':
            if stack:
                if stack[-1]=='(':
                    
                    stack.pop()
                else:
                    
                    stack.append(item)
            else:
                print("no")
                flag = 1
                break
        elif item =='[':
            stack.append(item)
            
        elif item ==']':
            if stack:
                if stack[-1]=='[':
                    
                    stack.pop()
                    
                else:
                    stack.append(item)
                    
            else:
                print("no")
                flag = 1
                break
    if flag==0:
        if stack:
            print("no")
        else :
            print("yes")