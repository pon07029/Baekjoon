import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
li=list(map(int, input().split()))
re=0
def f(arr):
    global re
    le=deque([])
    l=len(arr)
    if l==1:
        return deque([arr[0]])
    mid=l//2
    left=f(arr[:mid])
    right=f(arr[mid:])
    while left and right:
        if left[0]>right[0]:
            re+=len(left)
            le.append(right.popleft())
        else:
            le.append(left.popleft())
    while left:
        le.append(left.popleft())
    while right:
        le.append(right.popleft())
    return le
f(li)
print(re)
