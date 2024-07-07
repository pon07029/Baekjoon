a, b= map(int, input().split())

li = [-1] *1000001
le =[a]
now =0
while li[b] ==-1:
    la =[]
    for i in le:
        if li[i] ==-1:
            li[i]=now
            if i*2 <=b*3:
                la.append(i*2)
            if i+1 <=b*3:  
              la.append(i+1)
            if i-1 >=0:  
              la.append(i-1)
    le = la
    now+=1
print(li[b])