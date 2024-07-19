ar1=[[False]*10 for _ in range(9)]
ar2=[[False]*10 for _ in range(9)]
ar3=[[False]*10 for _ in range(9)]
li=[]
for i in range(9):
    li.append(list(map(int, input().strip())))

zero = []
for i in range(9):
    for j in range(9):
        if li[i][j]==0:
            zero.append((i,j))
        else:
            ar1[i][li[i][j]]=True
            ar2[j][li[i][j]]=True
            ar3[i//3*3+j//3][li[i][j]]=True

def f(n):
    if n==len(zero):
        for i in range(9):
            for j in range(9):
                print(li[i][j], end="")
            print("")
        exit()
    i,j=zero[n]
    for k in range(1,10):
            if not ar1[i][k] and not ar2[j][k] and not ar3[i//3*3+j//3][k]:
                ar1[i][k]=ar2[j][k]=ar3[i//3*3+j//3][k]=True
                li[i][j]=k
                f(n+1)
                li[i][j]=0
                ar1[i][k]=ar2[j][k]=ar3[i//3*3+j//3][k]=False


f(0)