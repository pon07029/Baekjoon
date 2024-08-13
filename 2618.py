import sys
input=sys.stdin.readline
N=int(input())
W=int(input())
li=[]
for i in range(W):
    a,b=map(int,input().split())
    li.append((a,b))
g={(1,1,N,N):0}
save={(1,1,N,N):[]}
mi=999
newmi=999
for i in range(W):
    n1, n2 = li[i]
    ng={}
    sv={}
    mmmi=newmi
    newmi=999999
    for k, v in g.items():
        a,b,c,d= k
        c1= abs(a-n1)+abs(b-n2)
        c2= abs(c-n1)+abs(d-n2)
        if v+c1<mmmi+2*N:
            if (n1,n2,c,d) in ng:
                if g[(a,b,c,d)]+c1<ng[(n1,n2,c,d)]:
                    ng[(n1,n2,c,d)]=g[(a,b,c,d)]+c1
                    sv[(n1,n2,c,d)]=save[(a,b,c,d)]+[True]
            else:
                ng[(n1,n2,c,d)]=g[(a,b,c,d)]+c1
                sv[(n1,n2,c,d)]=save[(a,b,c,d)]+[True]
        if v+c2<mmmi+2*N:
            if (a,b,n1,n2) in ng:
                if g[(a,b,c,d)]+c2<ng[(a,b,n1,n2)]:
                    ng[(a,b,n1,n2)]=g[(a,b,c,d)]+c2
                    sv[(a,b,n1,n2)]=save[(a,b,c,d)]+[False]
            else:
                ng[(a,b,n1,n2)]=g[(a,b,c,d)]+c2
                sv[(a,b,n1,n2)]=save[(a,b,c,d)]+[False]
        newmi=min(newmi,v+c1,v+c2)
    g=ng
    save=sv
mi=99999999
# print(g)
tt=(0,0,0,0)
for k,v in g.items():
    if mi>v:
        mi=v
        tt=k
print(mi)
for i in save[tt]:
    if i:
        print(1)
    else:
        print(2)