a, b = map(int, input().split())
q =[b]
n=1
while q:
    tmp=[]
    for i in q:
        if i == a:
            print(n)
            exit()
        if i%2 == 0 and i!=0:
            tmp.append(i//2)
        if i%10 == 1:
            tmp.append(i//10)

    n+=1
    q = tmp
print(-1)