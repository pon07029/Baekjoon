n = int(input())

li = [[" "]*(n*2-1) for _ in range(n)]

def f(i,j,s):
    if s==3:
        li[i][j]="*"
        li[i+1][j-1]="*"
        li[i+1][j+1]="*" 
        for k in range(5):
            li[i+2][j-2+k]="*"
    else:
        f(i,j,s//2)
        f(i+s//2,j-s//2,s//2)
        f(i+s//2,j+s//2,s//2)
f(0, n-1, n)
for i in li:
    print("".join(i))

