n=input()

def f(ar):
    if len(ar)==3:
        if ar[0]==ar[1]==ar[2]:
            return 2
        elif ar[0]==ar[1] or ar[0]==ar[2] or ar[1]==ar[2]:
            return 1
        return 0
    else:
        if ar[0]==ar[1]:
            return 2
        else:
            return 0


li=[]
for i in range(len(n)+1):
    li.append([])

def ff(k, arr=[]):
    if k<2:
        return (0, arr)
    if li[k]!=[]:
        return li[k]
    a, ar1 = ff(k-2, arr+[k-2])
    a+=+ f(n[k-1:k+1])
    b, ar2= ff(k-3, arr+[k-3])
    b+=f(n[k-2:k+1])
    if a>=b:
        p=a
        li[k]=(a, ar1)
        return (p, ar1)
    else:
        p=b
        li[k]=(b, ar2)
        return (p, ar2)
l=len(n)
print(ff(l-3,[l-3]), ff(l-2,[l-2]), ff(l-1,[l-1]))
    

