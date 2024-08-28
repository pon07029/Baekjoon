N, H, S=map(int,input().split())
f=list(map(int, input().split()))
r1=0
start, end=0,S*2/N
if end>H:
    start=end-H
    end=H
cha =(end-start)/N
for i in range(N):
    r1+=f[i]*(start*2+(2*i+1)*cha)
start, end=end,start
r2=0
for i in range(N):
    r2+=f[i]*(start*2-(2*i+1)*cha)
# print(start,end,cha)
re=min(r1, r2)/2
print(f"{re:.6f}")

    