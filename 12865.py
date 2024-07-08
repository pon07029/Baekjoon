import sys
N, K = map(int, sys.stdin.readline().split())
li=[]
for i in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))
li.sort(key=lambda x: x[0])
re=[[0, []] for i in range(K+1)]

for i in range(1,K+1):
    for j in range(N):
        if li[j][0]<=i:
            if re[i-li[j][0]][0]+li[j][1]>re[i][0] and j not in re[i-li[j][0]][1]:
                re[i][0] = re[i-li[j][0]][0]+li[j][1]
                re[i][1]= re[i-li[j][0]][1]+[j]
                
re.sort(key=lambda x: x[0])
print(re[-1][0])
