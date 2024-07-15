N, P, Q, X, Y = map(int, input().split())
g={}
def f(n):
    if n<= 0:
        return 1
    if n in g:
        return g[n]
    g[n]=f(n//P-X)+f(n//Q-Y)
    return g[n]
print(f(N))
