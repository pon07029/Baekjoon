# 세그먼트 트리
import sys
input = sys.stdin.readline
N =int(input())
l = []
segment_tree = [(1000000001,1000000000)]*(N*4)

def f(one, two):
    v1, s1 = one
    v2, s2 = two
    if v1==v2:
        return v1,min(s1,s2)
    if v1<v2:
        return v1,s1
    else:
        return v2,s2    


def init(start, end, index):
    if start == end:
        segment_tree[index] = (l[start-1], start)
        return segment_tree[index]
	
    mid = (start+end) // 2
    segment_tree[index] = f(init(start, mid, index*2), init(mid+1, end, index*2+1))
    return segment_tree[index]

def find(start, end, index, left, right):
    if start > right or end < left:
        return (1000000001,start)
        
    if start >= left and end <= right:
        return segment_tree[index]

    mid = (start + end) // 2
    sub_sum = f(find(start, mid, index*2, left, right), find(mid+1, end, index*2+1, left, right))
    return sub_sum

def update(start, end, index, update_idx, update_data):
    if start > update_idx or end < update_idx:
        return segment_tree[index]
    if start == end:
        segment_tree[index] = (update_data, start)
        return segment_tree[index]
    mid = (start + end) // 2
    update(start, mid, index*2, update_idx, update_data)
    update(mid+1, end, index*2+1, update_idx, update_data)
    segment_tree[index] = f(segment_tree[index*2], segment_tree[index*2+1])
    return segment_tree[index]
l=list(map(int,input().split()))

init(1, N, 1)
M=int(input())
for _ in range(M):
    a, b, c = map(int,input().split())
    if a == 1:
        update(1, N, 1, b, c)

    elif a == 2:
        print(find(1, N, 1, b, c)[1])
