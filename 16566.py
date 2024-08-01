import sys
from bisect import bisect_right
input=sys.stdin.readline
N, M, K = map(int, input().split())
card=list(map(int, input().split()))
card.sort()
ch=list(map(int, input().split()))
vi=[True]*M
for i in ch:
    index=bisect_right(card, i)
    for j in range(index, N):
        if vi[j]:
            vi[j]=False
            print(card[j])
            break