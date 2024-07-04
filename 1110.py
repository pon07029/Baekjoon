import math
def lcm(a, b, c):
    d= a * b // math.gcd(a, b)

    return d * c // math.gcd(d, c)

re =[]
dat = list(map(int, input().split()))
l = len(dat)
for i in range(l):
    for j in range(i+1, l):
        for k in range(j+1, l):
            re.append(lcm(dat[i], dat[j], dat[k]))

print(min(re))

