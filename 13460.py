import sys
input=sys.stdin.readline
N,M=map(int,input().split())
arr=[list(input()) for _ in range(N)]
B=(0,0)
R=(0,0)
for i in range(N):
    for j in range(M):
        if arr[i][j]=="B":
            B=(i,j)
        if arr[i][j]=="R":
            R=(i,j)
a,b=B
c,d=R
count=0
li=[(a,b,c,d)]
def down(a,b,c,d):
    global count
    a1,b1,c1,d1=a,b,c,d
    dx,dy=1,0
    kk=0
    ttmp="."
    if a<=c:
        while arr[c1+dx][d1+dy]==".":
            c1+=dx
            d1+=dy
        if arr[c1+dx][d1+dy]=="O":
            kk+=1
            ttmp="O"
        else:
            arr[c1][d1]="#"
        arr[c1][d1]="#"
        while arr[a1+dx][b1+dy]==".":
            a1+=dx
            b1+=dy
        if arr[a1+dx][b1+dy]=="O":    
            kk+=1
            return (0,0,0,0)
        arr[c1][d1]=ttmp
        if kk==1:
            print(count)
            exit()
        return (a1,b1,c1,d1)
    else:
        while arr[a1+dx][b1+dy]==".":
            a1+=dx
            b1+=dy
        if arr[a1+dx][b1+dy]=="O":
            return (0,0,0,0)
        arr[a1][b1]="#"
        while arr[c1+dx][d1+dy]==".":
            c1+=dx
            d1+=dy
        if arr[c1+dx][d1+dy]=="O":
            print(count)
            exit()
        arr[a1][b1]="."
        return (a1,b1,c1,d1)

def up(a,b,c,d):
    global count
    a1,b1,c1,d1=a,b,c,d
    dx,dy=-1,0
    kk=0    
    ttmp="."
    if a>=c:
        while arr[c1+dx][d1+dy]==".":
            c1+=dx
            d1+=dy
        if arr[c1+dx][d1+dy]=="O":
            kk+=1
            ttmp="O"
        else:
            arr[c1][d1]="#"
        while arr[a1+dx][b1+dy]==".":
            a1+=dx
            b1+=dy
        if arr[a1+dx][b1+dy]=="O":  
            kk+=1  
            return (0,0,0,0)
        arr[c1][d1]=ttmp
        if kk==1:
            print(count)
            exit()
        return (a1,b1,c1,d1)
    else:
        while arr[a1+dx][b1+dy]==".":
            a1+=dx
            b1+=dy
        if arr[a1+dx][b1+dy]=="O":
            return (0,0,0,0)
        arr[a1][b1]="#"
        while arr[c1+dx][d1+dy]==".":
            c1+=dx
            d1+=dy
        if arr[c1+dx][d1+dy]=="O":
            print(count)
            exit()
        arr[a1][b1]="."
        return (a1,b1,c1,d1)

def right(a,b,c,d):
    global count
    a1,b1,c1,d1=a,b,c,d
    dx,dy=0,1
    kk=0
    ttmp="."
    if d>=b:
        while arr[c1+dx][d1+dy]==".":
            c1+=dx
            d1+=dy
        if arr[c1+dx][d1+dy]=="O":
            kk+=1
            ttmp="O"
        else:
            arr[c1][d1]="#"
        while arr[a1+dx][b1+dy]==".":
            a1+=dx
            b1+=dy
        if arr[a1+dx][b1+dy]=="O":    
            kk+=1
            return (0,0,0,0)
        arr[c1][d1]=ttmp
        if kk==1:
            print(count)
            exit()
        return (a1,b1,c1,d1)
    else:
        while arr[a1+dx][b1+dy]==".":
            a1+=dx
            b1+=dy
        if arr[a1+dx][b1+dy]=="O":
            return (0,0,0,0)
        arr[a1][b1]="#"
        while arr[c1+dx][d1+dy]==".":
            c1+=dx
            d1+=dy
        if arr[c1+dx][d1+dy]=="O":
            print(count)
            exit()
        arr[a1][b1]="."
        return (a1,b1,c1,d1) 

def left(a,b,c,d):
    global count
    a1,b1,c1,d1=a,b,c,d
    dx,dy=0,-1
    kk=0
    ttmp="."
    if d<=b:
        while arr[c1+dx][d1+dy]==".":
            c1+=dx
            d1+=dy
        if arr[c1+dx][d1+dy]=="O":
            kk+=1
            ttmp="O"
        else:
            arr[c1][d1]="#"
        while arr[a1+dx][b1+dy]==".":
            a1+=dx
            b1+=dy
        if arr[a1+dx][b1+dy]=="O":    
            kk+=1
            return (0,0,0,0)
        arr[c1][d1]=ttmp
        if kk==1:
            print(count)
            exit()
        return (a1,b1,c1,d1)
    else:
        while arr[a1+dx][b1+dy]==".":
            a1+=dx
            b1+=dy
        if arr[a1+dx][b1+dy]=="O":
            return (0,0,0,0)
        arr[a1][b1]="#"
        while arr[c1+dx][d1+dy]==".":
            c1+=dx
            d1+=dy
        if arr[c1+dx][d1+dy]=="O":
            print(count)
            exit()
        arr[a1][b1]="."
        return (a1,b1,c1,d1) 

for i in range(10):
    count+=1
    tmp=[]
    for a,b,c,d in li:
        tmp.append(down(a,b,c,d))
        tmp.append(up(a,b,c,d))
        tmp.append(right(a,b,c,d))
        tmp.append(left(a,b,c,d))
    li=list(set(tmp))

print(-1)