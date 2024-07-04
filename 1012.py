import sys 
x=0
y=0
re=[]
li =[[]]
def check(x1, y1):
    if x1>=x:
        return False
    if y1>=y:
        return False
    if x1<0:
        return False
    if y1<0:
        return False
    return True

        
for i in range(int(input())):
    x, y, z = map(int, sys.stdin.readline().split())
    tmp=0
    tmpli=[]
    li = [[0 for j in range(y)] for i in range(x)]
    for j in range(z):
        a, b = map(int, sys.stdin.readline().split())
       
        li[a][b] = 1
    for j in range(x):
        for k in range(y):
            if li[j][k] == 1: 
                li[j][k] = 0
                tmpli.append([j, k])
                tmp+=1
                while len(tmpli) != 0:
                    
                    a, b = tmpli.pop()
                    if check(a+1, b):
                        if li[a+1][b] == 1:
                            li[a+1][b] = 0
                            tmpli.append([a+1, b])
                    if check(a-1, b):
                        if li[a-1][b] == 1:
                            li[a-1][b] = 0
                            tmpli.append([a-1, b])
                    if check(a, b+1):
                        if li[a][b+1] == 1:
                            li[a][b+1] = 0
                            tmpli.append([a, b+1])
                    if check(a, b-1):
                        if li[a][b-1] == 1:
                            li[a][b-1] = 0
                            tmpli.append([a, b-1])
    re.append(tmp)             


print(*re, sep="\n")
       
    