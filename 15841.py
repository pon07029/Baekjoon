
def fibo(n):
    if len(li) > n:
        return li[n]
    while len(li) <= n:
        li.append(li[-1] + li[-2])
    return li[-1]
li= [0,1]

while 1:
    n = int(input())
    if n == -1:
        break
    print(f"Hour {n}: {fibo(n)} cow(s) affected")
    
