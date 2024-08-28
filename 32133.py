import copy
N,M,K=map(int,input().split())
li=[]
for i in range(N):
    li.append(input())
mindepth=51
re=[]
def f(arr, depth):
    if depth>M:
        return
    # print(arr, depth)
    global re, K, mindepth
    if len(arr)==0:
        return
    if len(arr)<=K and depth<mindepth:
        # print(arr, depth)
        re=copy.deepcopy(arr)
        mindepth=depth
        return
    if depth==M:
        return
    P,S,R =[], [], []
    for w in arr:
        if w[depth]=='P':
            P.append(w)
        elif w[depth]=='S':
            S.append(w)
        elif w[depth]=='R':
            R.append(w)
    if P:
        f(P, depth+1)
    if S:
        f(S, depth+1)
    if R:
        f(R, depth+1)
f(li, 0)
# print(re)
# print(mindepth)
if mindepth==51:
    print(-1)
    exit()
print(mindepth)
for i in re[0][0:mindepth]:
    if i=='P':
        print('R',end='')
    elif i=='S':
        print('P',end='')
    elif i=='R':
        print('S',end='')
