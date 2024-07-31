import sys
N = int(sys.stdin.readline())
arr=[(0,0)]*N

for i in range(N):
    arr[i]=tuple(map(int,sys.stdin.readline().split()))
arr.sort(key=lambda x:x[0])

dat = [0]*N
dd=[0]*N
for i in range(N):
    a,b=arr[i]
    dat[i]=b
    dd[i]=a

li=[-1]*(N+1)

ll=[]
start=0
end=-1
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

for i in range(N):
    
    index = binary_search(dat[i], start, end)
    if index > end:
        end += 1
        li[end] = dat[i]
    else:
        li[index] = dat[i]
    ll.append((index, i))
      
kk=[True]*N
a=0
for i in range(len(ll), -1, -1):
    j,k = ll[i-1]
    if j == end:
        end -= 1
        kk[k]=False
        a+=1
print(N-a)
for i in range(N):
    if kk[i]:
        print(dd[i])

