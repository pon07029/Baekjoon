a, b= map(int, input().split())

c = (a+3)//4
d = (b+3)//4
le = [c,d]
li = [a%4 if a%4 !=0 else 4, b%4 if b%4 !=0 else 4]
print((max(le)-min(le)+max(li)-min(li)))
