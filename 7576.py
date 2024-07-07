import sys
x, y = map(int, sys.stdin.readline().split())
li= []
for i in range(y):
    li.append(list(map(int, sys.stdin.readline().split())))



# 좌우 상하 리턴
def f(a, b):
   
    ll = []
    if a-1 >=0:
        ll.append([a-1, b])
    if a+1 < y:
        ll.append([a+1, b])
    if b-1 >=0:
        ll.append([a, b-1])
    if b+1 < x:
        ll.append([a, b+1])
    lg =[]
    for i in ll:
        if li[i[0]][i[1]] == 0:
            lg.append(i)
    return lg 

day =0
lis = []
for i in range(x):
      for j in range(y):
          if li[j][i] == 1:
              for k in f(j, i):
                  lis.append(k) 
lis = list(set([tuple(i) for i in lis]))
while lis:
    day+=1
    ll = []
    for i in lis:
        li[i[0]][i[1]] = 1
    for i in lis:
        for k in f(i[0], i[1]):
            ll.append(k)
    ll = list(set([tuple(i) for i in ll]))
    lis =ll
    if not ll:
        break  

for i in range(x):
      for j in range(y):
          if li[j][i] == 0:
              day =-1
              break
print(day)