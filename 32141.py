N, H =map(int,input().split())
li=list(map(int, input().split()))
for i in range(N):
    H-=li[i]
    if H<=0:
        print(i+1)
        exit()
print(-1)