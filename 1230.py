O =input()
N= input()
Ol=len(O)
Nl=len(N)
li=[[0]*(Ol) for _ in range(Nl)]
dp=[[0]*(Ol) for _ in range(Nl)]
for i in range(Ol):
    for j in range(i,Nl):
        if N[j]==O[i]:
            dp[j][i]=1

# print(*dp,sep="\n")
if Ol>Nl:
    print(-1)
    exit()


def f(a,b):
    if b>=Ol:
        return 0
    if a>=Nl:
        return 100000
    if li[a][b]:
        return li[a][b]
    tmp=[]
    if dp[a][b]:
        # print("a",a,b)  
        if a==Nl-1 and b==Ol-1:
            # print("b",a,b)
            return 0
        if a!=Nl-1 and b==Ol-1:
            # print("a",a,b)
            return 1
        tmp.append(f(a+1,b+1))
            
    for i in range(Nl-Ol+b, a,-1 ):
        if dp[i][b]:
            p=f(i+1,b+1)+1

            tmp.append(p)
            if p<99999:
                break
    if not tmp:
        li[a][b]=100000
        return li[a][b]
    li[a][b]=min(tmp)
    return li[a][b]
pp=f(0,0)
print(pp if pp<99999 else -1)
# print(*li,sep="\n")
