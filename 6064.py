
re =[]
def fun(M,N,x,y):

    for i in range(N+1):
        if (i*M+x)%N == y%N:
            return i*M+x
    return -1
     


for i in range(int(input())):
    a, b, c, d = map(int, input().split())
    re.append(fun(a, b, c, d))
print(*re, sep="\n")