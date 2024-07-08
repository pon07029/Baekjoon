import sys
bf =[]

mxx =[]
mnn =[]
for i in range(int(sys.stdin.readline())):
    now =list(map(int, sys.stdin.readline().split()))
    if i == 0:
        mxx = [now[0], now[1], now[2]]
        mnn = [now[0], now[1], now[2]]
    else:
        mxx =[max(mxx[0], mxx[1])+now[0], max(mxx[0], mxx[1], mxx[2])+now[1], max(mxx[1], mxx[2])+now[2]]
        mnn =[min(mnn[0], mnn[1])+now[0], min(mnn[0], mnn[1], mnn[2])+now[1], min(mnn[1], mnn[2])+now[2]]
    bf =[[now[0], now[1], now[2]]]
print(max(mxx), min(mnn)) 

