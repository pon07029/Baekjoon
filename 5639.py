from collections import deque
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
li=[]
g={}
while True:
    try:
        i=int(input())
        li.append(i)
    except:
        break

def f(now,ar):
    left=-1
    right=-1
    if len(ar)==1:
        g[now]=[".","."]
        return
    for i in range(1,len(ar)):
        if ar[i]<ar[0] and left==-1:
            left=i
        if ar[i]>ar[0]:
            right=i
            break
    if left!=-1 and right!=-1:
        g[now]=[ar[left],ar[right]]
        f(ar[right],ar[right:])
        f(ar[left],ar[1:right])
        return
    if left!=-1:
        g[now]=[ar[left],"."]
        f(ar[left],ar[1:])
        return
    if right!=-1:
        g[now]=[".",ar[right]]
        f(ar[right],ar[1:])
        return
f(li[0],li)
def ff(n):
    if n == ".":
        return
    ff(g[n][0])
    ff(g[n][1])
    print(n)  
ff(li[0])

