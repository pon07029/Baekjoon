import sys
arr =[]
a, b = map(int, sys.stdin.readline().split())
are = [[-1]*b for _ in range(a)]
for i in range(a):
  arr.append(list(map(int, sys.stdin.readline().split())))
le =[]

# 상하좌우 1이면 반환
def f(y, x):
   
    ll = []
    if y-1 >=0:
        ll.append([y-1, x])
    if y+1 < a:
        ll.append([y+1, x])
    if x-1 >=0:
        ll.append([y, x-1])
    if x+1 < b:
        ll.append([y, x+1])
    lg =[]
    for i in ll:
        if arr[i[0]][i[1]] == 1 and are[i[0]][i[1]] == -1:
            lg.append(i)
    return lg 


for i in range(a):
  for j in range(b):
    if arr[i][j] == 2:
      le.append([i, j])

leng = 0
while le:
    ll = []
    for i in le:
        for j in f(i[0], i[1]):
            ll.append(j)
    ll = list(set([tuple(i) for i in ll]))
    for i in le:
        are[i[0]][i[1]] = leng
    le =ll
    if not ll:
        break  
    leng+=1

for i in range(a):
    for j in range(b):
        if arr[i][j] == 0:
            are[i][j] = 0
        
for i in range(a):
    print(*are[i])