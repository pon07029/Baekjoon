
import sys
input=sys.stdin.readline
N, M, K1, K2 = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(K1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)

selected = [-1] * (M)
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
re1,re2 = 0,0 
for i in range(N):            
    visited = [False] * (N)      
    if bimatch(i):
        re1 += 1
graph = [[] for _ in range(N)]
selected = [-1] * (M)
for i in range(K2):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
for i in range(N):            
    visited = [False] * (N)      
    if bimatch(i):
        re2 += 1
if re1<re2:
    print("네 다음 힐딱이")
else:
    print("그만 알아보자")