dat= list(map(int, input()))
li=[ 0 for _ in range(len(dat)+1)]
li[0], li[1]=1,1
if dat[0]==0:
    print(0)
else:
    for i in range(1, len(dat)):
        if dat[i]>0:
            li[i+1]+=li[i]
        if 10<= dat[i-1]*10+dat[i]<=26:
                li[i+1]+=li[i-1]
    print(li[-1]%1000000)