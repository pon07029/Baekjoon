T=int(input())
def f():
    N, W = map(int, input().split())
    ar1= list(map(int, input().split()))
    ar2= list(map(int, input().split()))
    li=[[0,0,0] for _ in range(N)]
    li[0]=(1,1,2)
    mi=999999
    if ar1[0]+ar2[0]<=W:
        li[0]=(1,1,1)
    if N==1:
        print(li[0][2])
        return
    if N==2:
        if ar1[0]+ar2[0]<=W and ar1[1]+ar2[1]<=W:
            print(2)
            return
        if ar1[0]+ar1[1]<=W and ar2[0]+ar2[1]<=W:
            print(2)
            return
        if ar1[0]+ar1[1]<=W:
            print(3)
            return
        if ar2[0]+ar2[1]<=W:
            print(3)
            return
        print(4)
        return  
    li[1]=[3,3,4]
    if li[0][2]==1 or ar1[0]+ar1[1]<=W:
        li[1][0]=2
    if li[0][2]==1 or ar2[0]+ar2[1]<=W:
        li[1][1]=2
    if (ar1[0]+ar1[1]<=W and ar2[0]+ar2[1]<=W) or (ar1[0]+ar2[0]<=W and ar1[1]+ar2[1]<=W):
        li[1][2]=2
    elif (ar1[1]+ar2[1]<=W):
        li[1][2]=min(li[1][0]+1, li[1][1]+1, li[0][2]+1)
    else:
        li[1][2]=min(li[1][0]+1, li[1][1]+1,li[0][2]+2)
    def ff():
        for i in range(2,N):
            if ar1[i]+ar1[i-1]<=W:
                li[i][0]=min(li[i-1][2]+1, li[i-1][1]+1)
            else:
                li[i][0]=min(li[i-1][2]+1, li[i-1][1]+2)
            if ar2[i]+ar2[i-1]<=W:
                li[i][1]=min(li[i-1][2]+1, li[i-1][0]+1)
            else:
                li[i][1]=min(li[i-1][2]+1, li[i-1][0]+2)
            if ar1[i]+ar2[i]<=W:
                li[i][2]=min(li[i-1][2]+1, li[i][1]+1, li[i][0]+1)
            else:
                li[i][2]=min(li[i-1][2]+2, li[i][1]+1, li[i][0]+1)
            if ar1[i]+ar1[i-1]<=W and ar2[i]+ar2[i-1]<=W:
                li[i][2]=min(li[i][2], li[i-2][2]+2)
    ff()
    # print(li)
    mi=min(mi,li[N-1][2])
    if N>2:
        li=[[0,0,0] for _ in range(N)]
        if ar1[0]+ar1[-1]<=W and ar2[0]+ar2[-1]<=W:
            li[0]=[0,0,0]
            li[1]=[1,1,2]
            if ar1[1]+ar2[1]<=W:
                li[1][2]=1
            ff()
            mi=min(mi,li[N-2][2]+2)
            # print(li)
        if ar1[0]+ar1[-1]<=W:
            li[0]=[0,1,1]
            li[1]=[2,2,3]
            if ar1[1]+ar2[1]<=W:
                li[1][2]=2
            if ar2[0]+ar2[1]<=W:
                li[1][1]=1
                li[1][2]=2
            ff()
            mi=min(mi, li[N-1][1]+1)
            # print(li)
        if ar2[0]+ar2[-1]<=W:
            li[0]=[1,0,1]
            li[1]=[2,2,3]
            if ar1[1]+ar2[1]<=W:
                li[1][2]=2
            if ar1[0]+ar1[1]<=W:
                li[1][0]=1
                li[1][2]=2
            ff()
            # print(li)

            mi=min(mi,  li[N-1][0]+1)
    print(mi)
               
for _ in range(T):
    f()
