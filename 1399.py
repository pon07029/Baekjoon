dy=[1, 0, -1, 0]
dx=[0, 1, 0, -1]

def dig(n):
    if n<10:
        return n
    return dig(n%10 + dig(n//10))

def one(k):
    na=k%4
    if na==0:
        return (0,0)
    if na==1:
        return (0,1)
    if na==2:
        return (1,1)
    if na==3:
        return (1,0)
def six(k,arr):
    na=k%12
    newarr=arr+arr
    x,y=0,0
    for i in range(na):
        d=i%4
        x+=dx[d]*newarr[i]
        y+=dy[d]*newarr[i]
    return (x,y)

def two(k,arr):
    na=k%4
    newarr=arr+arr
    x,y=0,0
    for i in range(na):
        d=i%4
        x+=dx[d]*newarr[i]
        y+=dy[d]*newarr[i]
    return (x,y)

def twoLast(k,arr):
    na=k%4
    newarr=[9,9,9,9,9,9]
    x,y=0,0
    for i in range(na):
        d=i%4
        x+=dx[d]*newarr[i]
        y+=dy[d]*newarr[i]
    if k>=1:
        y-=8
    if k>=2:
        x=x-9+arr[1]   
    return (x,y)

def three(k,arr):
    na=k%12
    newarr=arr+arr+arr+arr
    x,y=0,0
    for i in range(na):
        d=i%4
        x+=dx[d]*newarr[i]
        y+=dy[d]*newarr[i]
    return (x,y)

def threeLast(k,arr):
    na=k%4
    newarr=[9,9,9,9,9]
    x,y=0,0
    for i in range(na):
        d=i%4
        x+=dx[d]*newarr[i]
        y+=dy[d]*newarr[i]
    if k>=1:
        y-=8
    if k>=2:
        x=x-9+arr[1]
    return (x,y)

def make(n):
    arr=[1]
    a=1
    while True:
        a=dig(a*n)
        if a in arr:
            # arr.append(a)
            break
        arr.append(a)
    return arr
# for i in range(1, 1001):
#     print(i, make(i))
def ff(k,m):
    ar=make(m)
    # print(ar)
    l=len(ar)
    if l==1:
        # print("one")
        return one(k)
    if l==2:
        if ar[-1]==9:
            return twoLast(k,ar)
        return two(k,ar)
    if l==3:
        if ar[-1]==9:
            return threeLast(k,ar)
        return three(k,ar)
    if l==6:
        return six(k,ar)
for i in range(int(input())):
    k,m=map(int,input().split())
    print(*ff(k,m))