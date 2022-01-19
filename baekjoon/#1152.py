import sys
str = sys.stdin.readline()
lst = str.split(' ')
if lst[0]=='':
    lst = lst[1:]
if lst[len(lst)-1]=='\n':
    lst = lst[:len(lst)-1]

print(len(lst))