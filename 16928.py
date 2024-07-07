from collections import deque
import sys

arr=[]

def move(num):
    for i in arr:
        if i[0] == num:
            return i[1]
    return num

def fun(num, st):
    li =[]
    for i in range(1, 7):
        k = move(num+i)
        if k <= 100:
            li.append([k, st+1])
    return li


def f():
    q =deque([(1, 0)])
    isin = [0]*101
    isin[1] = 1
    while q:
        num, st = q.popleft()
        if num == 100:
            return st
        for i in fun(num, st):
            if isin[i[0]] == 0:
                isin[i[0]] = 1
                q.append(i)

for _ in range(sum(map(int, sys.stdin.readline().split()))):
    a ,b = map(int, sys.stdin.readline().split())
    arr.append([a, b])
print(f())