import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n=int(input())
ino = list(input().split())
pos = list(input().split())
li=[]
# def f(ar1, ar2,l):
#     if l==0:
#         return
#     if l==1:
#         li.append(ar1[0])
#         return
#     last=ar2[l-1]
#     li.append(last)
#     idx=ar1.index(last)
#     f(ar1[:idx],ar2[:idx],idx)
#     f(ar1[idx+1:],ar2[idx:l-1],l-idx-1)

def f(st1,ed1,st2, ed2, l):
    if l==0:
        return
    if l==1:
        # li.append(ino[st1])
        print(ino[st1],end=' ')
        return
    last=pos[st2+l-1]
    # li.append(last)
    print(last,end=' ')
    idx=ino.index(last,st1,ed1+1)
    f(st1,idx,st2,st2+idx-st1,idx-st1)
    f(idx+1,ed1,st2+idx-st1,ed2-1,l-idx-1+st1)
f(0,n,0,n,n)
# print(' '.join(li))
