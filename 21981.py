import sys
from functools import reduce


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
input= sys.stdin.readline
def f():
    n= int(input())
    T= list(map(str, input().split()))
    na=list(map(int, input().split()))
    for i in range(n):
        T[i]=int(T[i][0:2])*60*24+int(T[i][3:5])*60+int(T[i][6:8])
    print(chinese_remainder(T,na))
f()
    