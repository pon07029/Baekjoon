import sys
input=sys.stdin.readline
N= int(input())
li=list(map(int, input().split()))
mx, idx=9999999999999999, -1
def binary_search(target, start,end):

    while start <= end:
        mid = (start + end) // 2 # 중간값

        if li[mid] == target:
            return mid 

        elif li[mid] > target: # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:                    # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return  start
start, end=0, N-1
while start<=end:
    newMax,newidx=0,0
    mid=(start+end)//2
    for i in range(N):
        k=li[i]*abs(i-mid)
        if newMax<k:
            newMax=k
            newidx=i
    # print(start, end, mid, newMax, newidx)
    if newMax<mx:
        mx=newMax
        idx=newidx
    if newidx<mid:
        end=mid-1
    elif newidx>mid:
        start=mid+1
    else:
        idx=newidx
        break
# print(start, end, mid, newMax, newidx)
print(mx)