import math
N =int(input())
def ff(n):
    if n>N:
        return 0
    return (math.comb(52-n,N-n)*math.comb(13,n//4)-ff(n+4))%10007
print(ff(4))

