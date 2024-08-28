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

A, B = map(int, input().split())
if A%2==0:
    A+=1
for i in range(A, B+1, 2):
    if isprime(i):
        print(i, end=' ')