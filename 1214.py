import math
D, P, Q= map(int,input().split())
if P<Q:
    P,Q=Q,P
if D%P==0:
    print(D)
    exit()
if D%Q==0:
    print(D)
    exit()
mi=P
lcm=math.lcm(P,Q)
for i in range(lcm//P+2):
    if i*P>D:
        mi=min(mi,i*P-D)
        break
    k=D-i*P
    if k%Q==0:
        print(D)
        exit()
    else:
        mi=min(mi,i*P+Q*(k//Q+1)-D)
print(mi+D)