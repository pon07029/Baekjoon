from math import gcd
from random import randint
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
        for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
            if not f(i, n):
                return False
        return True

def g(x, n, r):
    return (x ** 2 + r) % n

def p(n): #pollard-rho
    if isprime(n):
        return n

    for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]:
        if not n % i:
            return i
    d = 1
    x = randint(2, n)
    y = x
    c = randint(1, n)
    while not d-1:
        y = g(g(y, n, c), n, c)
        x = g(x, n, c)
        t = abs(x - y)
        d = gcd(t, n)

        if d == n:
            return p(n)
    if isprime(d):
        return d
    return p(d)

n=int(input())
l=[]
while n>1:
    a = p(n)
    l.append(a)
    n //= a
l.sort()
print(*l, sep='\n')
