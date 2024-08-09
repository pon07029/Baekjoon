# 세그먼트 트리
import sys
input = sys.stdin.readline



l = list(map(int,input().split()))
N= l[0]
segment_tree = [(0,0)]*(N*4)
mx=0
def init(start, end, index):
    global mx
    if start == end:
        segment_tree[index] = (l[start-1],1)
        return segment_tree[index]
    mid = (start+end) // 2
    a1,a2   = init(start, mid, index*2)
    b1,b2   = init(mid+1, end, index*2+1)
    segment_tree[index] = (min(a1,b1),a2+b2)
    mx=max(mx,segment_tree[index][0]*segment_tree[index][1])
    return segment_tree[index]
init(1, N, 1)
print(mx)
