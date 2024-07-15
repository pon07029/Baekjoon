li=[1,1]

def f(nu):
    for i in range(len(li), nu+1):
        if i%2==0:
            s=0
            for j in range(0, i//2+1):
                s+=li[j]
            li.append(s)
        else:
            s=0
            for j in range(0, i//2+1):
                s+=li[j]
            li.append(s)
    

for i in range(int(input())):
    n= int(input())
    if n<len(li):
        print(li[n])
    else:
        f(n)
        print(li[n])