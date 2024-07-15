
def fibo(n):
    if len(li) > n:
        return li[n]
    while len(li) <= n:
        li.append(li[-1] + li[-2])
    return li[-1]
li= [1,1]

for i in range(int(input())):
    print(fibo(int(input())))
    
