import sys
a= int(sys.stdin.readline())
b= int(sys.stdin.readline())
dat = list(sys.stdin.readline())

li=[]
le =0
i=0
re=0
while i<(len(dat)-2):
    if dat[i:i+3] == ["I","O","I"]:
        le+=2
        i+=2
        continue
    else:
        i+=1
        if le>0:
            li.append(le)
            le =0
li.append(le)

for j in li:
    k = (j-(2*a))//2+1
    if k>0:
        re +=k

print(re)