import sys
input=sys.stdin.readline
N,S= map(int,input().split())
li=[]
for i in range(N):
    a,b=map(int,input().split())
    li.append((a,b))
li.sort(key=lambda x:x[0])
ar1=[0]*(N)
ar2=[0]*(N)
ar1[0], ar2[0]=li[0]


def binary_search(target,end):
    start=0
    while start <= end:
        mid = (start + end) // 2 # 중간값

        if li[mid][0] > target: # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:                    # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return  end

for i in range(1,N):
    e =binary_search(li[i][0]-S,i-1)
    if e==-1:
        if ar2[i-1]<li[i][1]:
            ar1[i], ar2[i]=li[i]
        else:
            ar1[i], ar2[i]=ar1[i-1], ar2[i-1]
    else:
        if ar2[e]+li[i][1]>ar2[i-1]:
            ar1[i], ar2[i]=ar1[e], ar2[e]+li[i][1]
        else:
            ar1[i], ar2[i]=ar1[i-1], ar2[i-1]

print(ar2[-1])
# print(*ar2)