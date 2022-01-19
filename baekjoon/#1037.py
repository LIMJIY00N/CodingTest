import sys
sys.stdin.readline()
line=sorted(map(int,sys.stdin.readline().split()))
print(line[-1]*line[0])
