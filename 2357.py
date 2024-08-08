import sys
input = sys.stdin.readline
N, M = map(int,input().split())
l = [0]*(N)
b=[0]*(N*4)
s=[999999999]*(N*4)


def big(start, end, index):
    if start == end:
        b[index] = l[start-1]
        return b[index]
	
    mid = (start+end) // 2
    b[index] = max(big(start, mid, index*2), big(mid+1, end, index*2+1))
    return b[index]

def small(start, end, index):
    if start == end:
        s[index] = l[start-1]
        return s[index]
	
    mid = (start+end) // 2
    s[index] = min(small(start, mid, index*2), small(mid+1, end, index*2+1))
    return s[index]

def findbig(start, end, index, left, right):
    if start > right or end < left:
        return 0

    if start >= left and end <= right:
        return b[index]

    mid = (start + end) // 2
    k = max(findbig(start, mid, index*2, left, right), findbig(mid+1, end, index*2+1, left, right))
    return k

def findsmall(start, end, index, left, right):
    if start > right or end < left:
        return 99999999999
        
    if start >= left and end <= right:
        return s[index]

    mid = (start + end) // 2
    k = min(findsmall(start, mid, index*2, left, right), findsmall(mid+1, end, index*2+1, left, right))
    return k

for _ in range(N):
    a=  int(input())
    l[_]=a

big(1, N, 1)
small(1, N, 1)
for _ in range(M):
    a1, b1 = map(int,input().split())
    print(findsmall(1, N, 1, a1, b1),findbig(1, N, 1, a1, b1),)