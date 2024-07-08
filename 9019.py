from collections import deque
import sys

def D(n):
    return n*2 % 10000
def S(n):
    return n-1 if n != 0 else 9999
def L(n):
    return n%1000*10+n//1000
def R(n):
    return n%10*1000+n//10



def fun(num, st):
    li =[]
    li.append([D(num), st+'D'])
    li.append([S(num), st+'S'])
    li.append([L(num), st+'L'])
    li.append([R(num), st+'R'])
    return li


def f(start, end):
    q =deque([[start, '']])
    isin = [0]*10000
    isin[start] = 1
    while q:
        num, st = q.popleft()
        if num == end:
            return st
        for i in fun(num, st):
            if isin[i[0]] == 0:
                isin[i[0]] = 1
                q.append(i)
for _ in range(int(sys.stdin.readline())):
    a ,b = map(int, sys.stdin.readline().split())
    print(f(a, b))