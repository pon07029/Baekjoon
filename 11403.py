import sys
g  = {}
N= int(input())
ar = [[0]*N for i in range(N)]
for i in range(N):
    dat = list(map(int, sys.stdin.readline().split()))
    for j in range(len(dat)):
       if dat[j] == 1:
          # ar[i][j] = 1
          if i in g:
              g[i].append(j)
          else:
              g[i] = [j]

def bfs(start_node):
    need_visited= [start_node]
  
    
    are= [[0]*N for i in range(N)]
    while need_visited:
        
        tmp =[]
        for i in need_visited:
            if i in g:
                for j in g[i]:
                    if are[i][j]!=1:
                        are[i][j] = 1
                        tmp.append(j)
                        ar[start_node][j] = 1
        need_visited = tmp
for i in range(N):
    bfs(i)
for i in range(N):
    print(*ar[i])

     