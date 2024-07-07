import sys
re=[0]
a, b = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split())) 
le =[]
for i in range(b):
    le.append(list(map(int, sys.stdin.readline().split()))) 
for i in li:
    re.append(re[-1]+i)

for i in le:
    print(re[i[1]]-re[i[0]-1])

