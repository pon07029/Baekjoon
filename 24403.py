ar=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
re=1
p=1
n=int(input())
li=[]
for i in range(len(ar)):
    if re*ar[i]>n:
        break
    re*=ar[i]
    li.append(ar[i])
for i in li:
    p*=i-1
for i in li:
        if p%i==0:
            p//=i
            re//=i
print(re-p,"/",re,sep="")