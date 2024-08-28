# pypy
import sys
input=sys.stdin.readline
def s():
    N, M= map(int, input().split())
    graph = [[] for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
    selected = [-1] * (N)
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
if __name__ == '__main__':
    s()
