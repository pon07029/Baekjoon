import sys
import math
input=sys.stdin.readline
N, M= map(int, input().split())
graph = [list(map(int, input().split()))[1:] for _ in range(N)]
selected = [-1] * (M)
def bimatch(N):                                           
    if visited[N]==2:                                        
        return False                                      
    visited[N] +=1                                                                    
    for num in graph[N]:                                   
        if selected[num] == -1:         
            selected[num] = N                                
            return True    
    for num in graph[N]:                                   
        if bimatch(selected[num]):                         
            selected[num] = N                                
            return True

    return False   
re = 0 
for i in range(N):            
    visited = [0] * (N)      
    if bimatch(i):
        re += 1
print(re)

def f(x):
    g={}
    while x != 1:
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    x = x // i
                    if i in g:
                        g[i] += 1
                    else:
                        g[i] = 1
                    break
            else:
                if x in g:
                        g[x] += 1
                else:
                        g[x] = 1
                break
    print(g)
    return g
f(re)