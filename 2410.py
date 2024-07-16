k = int(input())
li=[]
re=[1]*(k+1)
tmp=2
while True:
    if tmp>k:
        break
    for i in range(tmp,k+1):
        re[i]+=re[i-tmp]%1000000000
    tmp*=2
# print(*re)
print(re[-1]%1000000000)