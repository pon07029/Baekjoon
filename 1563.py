N = int(input())
li=[1,1,0,1,0,0]
for i in range(N-1):
    tm=li
    tmp=[0,0,0,0,0,0]
    tmp[0]= (tm[0]+tm[1]+tm[2])%1000000
    tmp[1]= tm[0]%1000000
    tmp[2]=tm[1]%1000000
    tmp[3]=(tmp[0]+tm[3]+tm[4]+tm[5])%1000000
    tmp[4]=tm[3]%1000000
    tmp[5]=tm[4]%1000000
    li=tmp
print(sum(li)%1000000)