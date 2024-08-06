
def f(s,p,b):
    t=0
    li=[0]*(p+1)
    for i in range(1,p//2+1):
        for j in range(2*i,p+1,i):
            li[j]+=i
    for i in range(s,p+1):
        if abs(li[i]-i)<=b:
            t+=1
    return t
n=0
while True:
    n+=1
    s,p,b=map(int,input().split())
    if s==0 and p==0 and b==0:
        break
    print(f"Test {n}: {f(s,p,b)}")