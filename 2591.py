W=list(input())
li= []
li.append([1,0])
for i in range(1, len(W)):
    tmp=[0,0]
    if W[i]=="0":
        tmp[1]=li[i-1][0]
    else:
        if int(W[i-1]+W[i])<=34:
            tmp[1]=li[i-1][0]
        tmp[0]=li[i-1][1]+li[i-1][0]
 
    li.append(tmp)
print(sum(li[-1]))
