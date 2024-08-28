import sys
input = sys.stdin.readline
N= int(input())
segment_tree = [0]*(N*4)

def find(start, end, index, left, right):
    if start > right or end < left:
        return 0
        
    if start >= left and end <= right:
        return segment_tree[index]

    mid = (start + end) // 2
    sub_sum = find(start, mid, index*2, left, right) + find(mid+1, end, index*2+1, left, right)
    return sub_sum

def update(start, end, index, update_idx):
    if start > update_idx or end < update_idx:
        return
    segment_tree[index] += 1
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index*2, update_idx)
    update(mid+1, end, index*2+1, update_idx)

ar1=list(map(int,input().split()))
g={}
for i in range(N):
    g[ar1[i]]=i+1
li=[]
for i in list(map(int,input().split())):
    li.append(g[i])
su=0
for i in li:
    su+=find(1, N, 1, i, N)
    update(1, N, 1, i)
print(su)


