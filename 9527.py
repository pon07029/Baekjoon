a,b=map(int,input().split())
save = [0 for _ in range(60)]  

for i in range(1, 60):  
    save[i] = 2**(i-1) + 2 * save[i-1]
def f(m):
    if m<4:
        if m==3:
            return 3
        elif m==2:
            return 1
        else:
            return 1
    k=format(m,"b")
    n=len(str(k))
    st=str(k)
    su=0
    for i in range(n-1):
        if st[i]=="1":
            su+=int("".join(st[i+1:]),2)+1
            # print(int("".join(st[i+1:]),2)+1)
            if i !=0:
                su+=save[n-i-1]
                # print(save[n-i-1])
        # if "".join(st[1:i]):
        #     if int("".join(st[1:i])):
        #         su+=int("".join(st[1:i]), 2)+1

            
    if st[-1]=="1":
        su+=1
    # su+=int("".join(st[1:n-1]),2)
    return su

def ff(e):
    if e==1:
        return 1
    return (e+1)*(2**(e-2))
re=0

for i in range(len(format(a,"b")), len(format(b,"b"))):
    re+=ff(i)
re+=f(b)
if len(bin(a))==len(bin(a-1)):
    re-=f(a-1)
if a==1:
    re+=1

print(re)