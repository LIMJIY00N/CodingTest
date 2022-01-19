line = input()
arr = ["lj","nj","c=","c-","dz=","d-","s=","z="]
for item in arr:
    line = line.replace(item,"*")

print(len(line))
