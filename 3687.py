import sys
input= sys.stdin.readline

g={
    2:"1", 3:"7", 4:"4", 5:"2", 6:"6", 7:"8", 8:"10", 9:"18", 10:"22",11:"20",
    12:"28", 13:"68", 14:"88", 15:"108", 16:"188", 17:"200", 18:"208", 19:"288",
}
li=[-1]*101

def big(n):
    if n%2==0:
        return "1"*(n//2)
    return "7"+"1"*((n-3)//2)

def sm(n):
    if n<20:
        return g[n]
    if li[n]!=-1:
        return li[n]
    else:
        li[n]= sm(n-7)+"8"
        return li[n]
for i in range(int(input())):
    k=int(input())
    print(sm(k), big(k))
