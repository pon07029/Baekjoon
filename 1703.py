import sys
re=[]
while True:
    sum=1
    dat = list(map(int, sys.stdin.readline().split()))  

    if dat[0] == 0:
        break
    for i in range(1, len(dat)):
        if i%2==1:
            sum*=dat[i]
        else:
            sum-=dat[i]
    re.append(sum)
print(*re, sep="\n")