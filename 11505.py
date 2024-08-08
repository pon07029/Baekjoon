# 세그먼트 트리
import sys
input = sys.stdin.readline
N, M, K = map(int,input().split())
l = []
segment_tree = [0]*(N*4)

def init(start, end, index):
    if start == end:
        segment_tree[index] = l[start-1]
        return segment_tree[index]
	
    mid = (start+end) // 2
    segment_tree[index] = (init(start, mid, index*2) * init(mid+1, end, index*2+1))%1000000007
    return segment_tree[index]

def find(start, end, index, left, right):
    if start > right or end < left:
        return 1
        
    if start >= left and end <= right:
        return segment_tree[index]

    mid = (start + end) // 2
    sub_sum = (find(start, mid, index*2, left, right) * find(mid+1, end, index*2+1, left, right))%1000000007
    return sub_sum

def update(start, end, index, update_idx, up):
    if start > update_idx or end < update_idx:
        return
    if start == end:
        segment_tree[index] = up
        return
    mid = (start + end) // 2
    update(start, mid, index*2, update_idx, up)
    update(mid+1, end, index*2+1, update_idx, up)
    segment_tree[index] = (segment_tree[index*2] * segment_tree[index*2+1])%1000000007

for _ in range(N):
    l.append(int(input()))

init(1, N, 1)
for _ in range(M+K):
    a, b, c = map(int,input().split())
    if a == 1:
        l[b-1] = c
        update(1, N, 1, b, c)
    elif a == 2:
        print(find(1, N, 1, b, c))
