import sys
a= int(sys.stdin.readline())
dat = list(map(int, sys.stdin.readline().split()))
li = []
for i in range(a):
    li.append([dat[i], i]) 
li.sort(key=lambda x : x[0])
bf = li[0][0]
li[0][0]=0
tmp =0
for i in range(1,a):
    if li[i][0]==bf:
        li[i][0]=tmp
    else:
        bf = li[i][0]
        tmp+=1
        li[i][0]=tmp
        
li.sort(key=lambda x : x[1])
print(*[i[0] for i in li])