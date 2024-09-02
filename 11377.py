# pypy
import sys
input=sys.stdin.readline
N, M= map(int, input().split())
graph = [list(map(int, input().split()))[1:] for _ in range(N)]
selected = [-1] * (M + 1)
def bimatch(N):                                           
    if visited[N]:                                        
        return False                                      
    visited[N] = True                                                                       
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
    visited = [False] * (N)      
    if bimatch(i):
        re += 1
print(re)
