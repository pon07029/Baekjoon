import sys 
a= int(sys.stdin.readline())
li = []
re = []
tt=[]
for i in range(a):
    li.append(int(sys.stdin.readline()))

for i in range(a):
    if i == 0:
        re.append([li[i]])
    elif i == 1:
        re.append([li[i], li[i]+li[i-1]])
    else:
        kk = []
        kk.append(max(re[i-2])+li[i])
        kk.append(re[i-1][0]+li[i])        
        re.append(kk)
  
print(max(re[-1]))
