import sys
dic ={}
for i in range(1,21):
    dic[i]=0
def fun(a):
    if a[0]== "add":
        dic[int(a[1])]=1
    elif a[0]== "remove":
        dic[int(a[1])]=0
    elif a[0]== "check":
        print(dic[int(a[1])])
    elif a[0]== "toggle":
        if dic[int(a[1])]==1:
            dic[int(a[1])]=0
        else:
            dic[int(a[1])]=1
    elif a[0]== "all":
        for i in range(1,21):
            dic[i]=1
    else:
        for i in range(1,21):
            dic[i]=0
for i in range(int(input())):
    dat = list(map(str, sys.stdin.readline().split()))  
    fun(dat)

