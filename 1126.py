import copy
N=int(input())
li=list(map(int, input().split()))
dp=[0]*500001
for i in range(N):
    h=li[i]
    
    tmp=[]
    for j in range(500001):
        if dp[j]:
            tmp.append(j)
    tmdp=copy.deepcopy(dp)
    for j in tmp:
            cha=abs(h-j)
            dp[cha]=max(tmdp[cha],h+tmdp[j]-j, tmdp[j])
            # print(cha,dp[cha],h+dp[j]-j, dp[j])
            hap=h+j
            dp[hap]=max(tmdp[hap],tmdp[j]+h)
            # print(hap, dp[hap])
    # print("--------------")
    dp[h]=max(dp[h],h)
    # print(dp[:30])
# print(dp[:30])
if dp[0]:
    print(dp[0])
else:
     print(-1)