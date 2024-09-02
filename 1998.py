import sys
input=sys.stdin.readline
N, M = map(int, input().split())
arr=[list(input()) for _ in range(N)]

re=0
def f(start, end):
    global re
    if start==end:
        re+=1
        return
    for i in range():
