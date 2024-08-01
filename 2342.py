list=list(map(int,input().split()))
tt=999999
arr=[[tt for k in range(5)] for _ in range(5)]
arr[0][0]=0
def f(now):
    global arr
    tmp=[]
    for i in range(5):
        for j in range(5):
            if arr[i][j]!=tt:
                tmp.append((i,j, arr[i][j]))
    tmparr=[[tt]*5 for _ in range(5)]
    for i,j,c in tmp:
        if i ==0 or j ==0:
                if i==0 and j==0:
                    tmparr[i][now]=min(tmparr[i][now],c+2)
                    continue
                elif i==0:
                    tmparr[now][j]=min(tmparr[now][j],c+2)
                else:
                    tmparr[now][i]=min(tmparr[now][i],c+2)
        if now==i:
            tmparr[i][j]=min(tmparr[i][j],c+1)
        elif now==j:
            tmparr[j][i]=min(tmparr[j][i],c+1)
        else:
                if abs(i-now)==2:
                    tmparr[now][j]=min(tmparr[now][j],c+4)
                else:
                    tmparr[now][j]=min(tmparr[now][j],c+3)
                if abs(j-now)==2:
                    tmparr[now][i]=min(tmparr[now][i],c+4)
                else:
                    tmparr[now][i]=min(tmparr[now][i],c+3)
    arr=tmparr
    return

for i in list:
    if i ==0:
        break
    f(i)
    # print(*arr, sep='\n')
    # print()
mi=tt
for i in range(5):
    mi=min(mi,min(arr[i]))
    
print(mi)
