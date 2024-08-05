N=int(input())
w=input()
now=int(input())
if w[0]=="i":
    if now%2==0:
        print(now)
    elif now>1:
        print(now-1)
    else:
        print(now+1)
else:
    if now%2==1:
        print(now)
    else:
        print(now-1)