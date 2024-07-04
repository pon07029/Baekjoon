import math

a, b= map(int, input().split())


c = math.gcd(a, b)
a = a // c
b = b // c


print(f"{b-a} {b}")