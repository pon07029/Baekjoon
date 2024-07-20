N= int(input())
dat = [list(input()) for i in range(N)]
for i in range(N):
    for j in range(N):
        dat[i][j] = int(dat[i][j])

def f(p,c):
    tmp=[]
    for i in range(N):
        if i==p:
            continue
        if dat[p][i]>=c:
            tmp.append((i,dat[p][i]))
    if not tmp:
        return 1
    else:
        return max([f(i,d) for i,d in tmp])+1

print(f(0,0))