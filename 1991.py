g={}
for i in range(int(input())):
    a,b,c = map(str, input().split())
    g[a] = [b,c]

def f(n):
    if n == ".":
        return
    print(n, end="")
    f(g[n][0])
    f(g[n][1])

def ff(n):
    if n == ".":
        return
    ff(g[n][0])
    ff(g[n][1])
    print(n, end="")   
def fff(n):
    if n == ".":
        return
    fff(g[n][0])
    print(n, end="") 
    fff(g[n][1])
      
f("A")
print("")
fff("A")
print("")
ff("A")