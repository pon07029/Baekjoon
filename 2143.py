T=int(input())
n=int(input())
ar1=list(map(int,input().split()))
m=int(input())
ar2=list(map(int,input().split()))
re=0
g1={}
su=[0]*n
su[0]=ar1[0]
for i in range(1,n):
    su[i]=su[i-1]+ar1[i]
for i in range(n):
    for j in range(i,n):
        if su[j]-su[i]+ar1[i] in g1:
            g1[su[j]-su[i]+ar1[i]]+=1
        else:
            g1[su[j]-su[i]+ar1[i]]=1
g2={}
su=[0]*m
su[0]=ar2[0]
for i in range(1,m):
    su[i]=su[i-1]+ar2[i]
for i in range(m):
    for j in range(i,m):
        if su[j]-su[i]+ar2[i] in g2:
            g2[su[j]-su[i]+ar2[i]]+=1
        else:
            g2[su[j]-su[i]+ar2[i]]=1
data= sorted(g2)
ed=len(data) - 1

def binary_search(target):
    start = 0 			# 맨 처음 위치
    end = ed 	# 맨 마지막 위치

    while start <= end:
        mid = (start + end) // 2 # 중간값

        if data[mid] == target:
            return mid 		# target 위치 반환

        elif data[mid] > target: # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:                    # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return mid

for k, v in g1.items():
    tar = T-k
    idx = binary_search(tar)
    if data[idx] == tar:
        re+=v*g2[tar]
print(re)