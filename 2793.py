import math
re=1
save=[0]*45
save[2]=1
li=[]
A,B=map(int,input().split())
for i in range(3,45):
    tmp=2
    while tmp<=i:
        if i%tmp==0:
            tmp+=1
        else:
            save[i]=save[tmp]+1
            break

for i in range(2,42):
    re=math.lcm(re,i)
    li.append((re,save[i+1]-save[i]))
# print(save)
# print(li)
tb=B*2-5
for i,j in li:
    tb+=(B//i)*j
A=A-1    
ta=A*2-5
for i,j in li:
    ta+=(A//i)*j
print(tb-ta)
