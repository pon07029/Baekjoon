li=[]
def fibo(n, p):
    a, b = 0, 1
    for _ in range(n):
        a, b = b%p, a+b%p
        if a ==b and _>0:
            li.append([p, _])
            break
    return a

for i in range(1, 100):
      fibo(300, i)

# print(*li, sep="\n")
for i in
