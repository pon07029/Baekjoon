import math
# 소수
a = int(input())
b = int(input())
le=[]
def sosu(n):
    chk = [True]*(n+1)
    res = []
    chk[0], chk[1] = False, False
    for i in range(2, int(math.sqrt(n))+1):
        if chk[i]:
            res.append(i)
            j = 2
            while i*j <= n:
                chk[i*j] = False
                j += 1
    res = [x for x in range(n+1) if chk[x]]
    return res
re = sosu(b)


for i in re:
  if i>=a:
    le.append(i)
if len(le)<1:
    print(-1)
else:
    print(sum(le))
    print(min(le))