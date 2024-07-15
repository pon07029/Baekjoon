N = int(input())
a = 0
li=[]
re=[]
s=1
for i in range(int(input())):
    b = int(input())
    if b-a-1>0:
        li.append(b-a-1)
    a=b
if N-a>0:
    li.append(N-a)

li.sort()
if len(li)==0:
    print(1)
    exit()

def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        re.append(b)
    return a
fibo(li[-1])
for i in li:
    s*=re[i-1]
print(s)