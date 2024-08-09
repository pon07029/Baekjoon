from functools import reduce
import math
import sys
from random import randrange
input = sys.stdin.readline

pli = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
def power(x,y,p):
    if y<2: return (x**y)%p
    else:
        d = y//2
        if y%2 == 0: return (power(x,d,p)**2)%p 
        else: return (x*(power(x,d,p))**2)%p
        
def mr(n,a):
    s,d = 0,n-1
    while d%2 == 0: s += 1; d //= 2
    x = power(a,d,n)
    if x == 1 or x+1 == n: return True
    for i in range(0, s-1):
        x = power(x,2,n)
        if x+1 == n: return True
    return False
 


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)  # n 값 모두 곱하기
    for n_i, a_i in zip(n, a):
        p = prod // n_i  # bar n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):  # Modular inverse
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1

def comb(n,m,p):
    if n<m: 
        return 0
    return math.comb(n,m)%p

def f(n,m,p):
    if n==0 or m==0: return 1
    return comb(n%p,m%p,p)*f(n//p,m//p,p)%p



li=[11,13,37]
for i in range(int(input())):
    N, K=map(int, input().split())
    a=[]
    b=[]
    for i in li:
        a.append(i)
        b.append(f(N, K, i))

    print(chinese_remainder(a, b))



