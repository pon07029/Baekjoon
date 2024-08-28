import sys
input=sys.stdin.readline
N= int(input())
li=list(map(int, input().split()))
graph=[[] for _ in range(N)]
mx=max(li)*2
sosu=[True]*(mx+1)
for i in range(2, int(mx**0.5)+1):
    if sosu[i]:
        for j in range(i+i, mx+1, i):
            sosu[j]=False
for i in range(N):
    for j in range(i+1, N):
        if sosu[li[i]+li[j]]:
            graph[i].append(j)
            graph[j].append(i)

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
se=set() 
for i in graph[0]:   
    selected = [-1] * N      
    selected[0] = i   
    selected[i] = 0
    re=1
    for j in range(1,N):
        visited = [False] * (N)  
        visited[0], visited[i] = True, True
        bimatch(j)
    ch=True
    for k in selected:
        if k==-1:
            ch=False
    if ch:
        se.add(li[selected[0]])
        # print(li[selected[0]], li[i])
        # print(selected)
# print(graph)
ll=list(se)
ll.sort()
print(-1 if not ll else ' '.join(map(str, ll)))