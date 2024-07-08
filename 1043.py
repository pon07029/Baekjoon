import sys
_, N = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))
h.pop(0)
h.sort()

li=[]
for i in range(N):
    dat = list(map(int, sys.stdin.readline().split()))
    dat.pop(0)
    dat.sort()
    tmp=False
    for i in h:
        for j in dat:
            if i<j:
                break
            if i==j:
                tmp=True
                break
        if tmp:
            break
    if tmp:
        h+=dat
    else:
        li.append(dat)
    h=list(set(h))
    h.sort()
tmpp=True
while tmpp:
    tmpp=False
    for i in range(len(li)):
        for j in h:
            if j in li[i]:
                h+=li[i]
                h=list(set(h))
                li.pop(i)
                tmpp=True
                break
        if tmpp:
            break

print(len(li))