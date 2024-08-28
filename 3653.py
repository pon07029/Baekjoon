import sys
input = sys.stdin.readline
def f():
    N, M = map(int,input().split())
    li=list(map(int,input().split()))
    segment_tree = [0]*(N*4)

    def init(start, end, index):
        if start == end:
            segment_tree[index] = start-1
            return segment_tree[index]
    
        mid = (start+end) // 2
        segment_tree[index] = min(init(start, mid, index*2) , init(mid+1, end, index*2+1))
        return segment_tree[index]

    def find(start, end, index, num):

        if start == num and end == num:
            return segment_tree[index]
        mid = (start + end) // 2
        if num <= mid:
            return find(start, mid, index*2, num)
        else:
            return find(mid+1, end, index*2+1, num)

    def update(start, end, index, update_idx, target):
        if start == end:
            if start == target:
                segment_tree[index] =0
            else:
                segment_tree[index] +=1
            return segment_tree[index]
        mid = (start + end) // 2
        if segment_tree[index*2] <= update_idx:
            update(start, mid, index*2, update_idx,target)
        if segment_tree[index*2+1] <= update_idx:
            update(mid+1, end, index*2+1, update_idx,target)
        segment_tree[index] = min(segment_tree[index*2], segment_tree[index*2+1])


    init(1, N, 1)

    for i in range(M):
        now = find(1, N, 1, li[i])
        update(1, N, 1, now, li[i])
        # print(segment_tree)
        print(now, end=' ')
    print()
for i in range(int(input())):
    f()
