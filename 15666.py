import sys
a, b=map(int, input().split())

dat = list(map(int, sys.stdin.readline().split()))
dat = list(set(dat))
dat.sort()
a=len(dat)
num=[]

def fun():
    if len(num) == b:
        print(*num)
        return
    for i in range(a):
        if len(num)>0 :
            if num[-1] > dat[i]:
                continue
      
        num.append(dat[i])
        fun()
        num.pop()
fun()
