import sys
input = sys.stdin.readline
def f(a, n): # 밀러-라빈
    d = n - 1
    r = 0
    while not d % 2:
        d //= 2
        r += 1
    x = pow(a, d, n)
    if x == 1 or x == n - 1:
        return True

    for i in range(r-1):
        x = pow(x, 2, n)
        if x == n - 1:
            return True

    return False
def isprime(n):
    if n <= 71:
        if n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]:
            return True
        else:
            return False
    else:
        for i in [2, 7,61]:
            if not f(i, n):
                return False
        return True
n=int(input())
re=0
for _ in range(n):
    a=int(input())
    if isprime(a*2+1):
        re+=1
print(re)