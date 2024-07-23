import sys
N=int(input())


li=[]
mx=0
for _ in range(N):
    li.append(int(sys.stdin.readline()))
if N==1:
    print(1)
    sys.exit()
li.sort()
dp={}
def binary_search(target, start):
    end = N-1
    while start <= end:
        mid = (start + end) // 2 # 중간값

        if li[mid] >= target:
            # print(target,start,mid)
            end=mid-1 

        else:                    # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return  start

for i in range(N-1):
    for j in range(i+1,N):
        count=2
        cha=li[j]-li[i]
        if (li[i],cha) in dp:
            continue
        next=li[j]+cha
        st=j+1
        while True:
            # print(i,j,next,st)
            st= binary_search(next,st)+1
            if st>N:
                break
            if next!=li[st-1]:
                break
            count+=1
            next+=cha
        dp[(li[i],cha)]=count
# print(mx)
print(max(dp.values()))
# print(binary_search(3,2))



