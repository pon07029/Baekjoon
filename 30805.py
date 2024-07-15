n1 =int(input())
l1 = list(map(int, input().split()))
n2=int(input())
l2 = list(map(int, input().split()))

def f(i1, j1):
    mx=0
    ii,jj=-1,-1
    for i in range(i1, n1):
        for j in range(j1, n2):
            if l1[i] == l2[j] and mx < l2[j]:
                mx = l2[j]
                # print(mx)
                ii,jj=i,j
    return ii,jj,mx
                

i1=-1
j1=-1
li=[]
while True:
    i1,j1,mx = f(i1+1,j1+1)
    if mx == 0:
        break
    else:
        li.append(mx)
print(len(li))
print(*li)