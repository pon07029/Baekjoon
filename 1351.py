N, P, Q = map(int, input().split())
g={}
def f(n):
    if n== 0:
        return 1
    if n in g:
        return g[n]
    g[n]=f(n//P)+f(n//Q)
    return g[n]
print(f(N))
