import sys
input=sys.stdin.readline
def f():
    N, M= map(int, input().split())
    li=[list(input()) for _ in range(N)]
    sit=[[0]*(M+2) for i in range(N+1)]
    six=[[0]*(M+2) for i in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            # if li[i-1][j-1]=='X':
                sit[i][j]=max(sit[i-1][j], six[i-1][j-1], six[i-1][j+1], sit[i-1][j])+1
                six[i][j]=max(sit[i][j-1], sit[i][j+1], sit[i-1][j-1], sit[i-1][j+1], sit[i-1][j])
                if i==1:
                    six[0][j]=six[1][j]
        for j in range(M, 0, -1):
            sit[i][j]=max(sit[i-1][j], six[i-1][j-1], six[i-1][j+1], sit[i-1][j])+1
            six[i][j]=max(sit[i][j-1], sit[i][j+1], sit[i-1][j-1], sit[i-1][j+1], sit[i-1][j])
                

    print(*sit, sep='\n')
    print()
    print(*six, sep='\n')
f()