ar1=list(input())
ar2=list(input())
be=[0]*len(ar2)
nindex=0
st=0
l1=len(ar1)
l2=len(ar2)

for i in range(1,l2):
    while st>0 and ar2[i]!=ar2[st]:
        st=be[st-1]
    if ar2[i]==ar2[st]:
        st+=1
        be[i]=st
start=0
p=0
re=[]
for i in range(l1):
    while start>0 and ar1[i]!=ar2[start]:
        start=be[start-1]
    if ar1[i]==ar2[start]:
        if start==l2-1:
            re.append(i-l2+2)
            start=be[start]
        else:
            start+=1
print(len(re))
print(*re,sep='\n')
