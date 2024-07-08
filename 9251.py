N = list(input(  ))
M = list(input(  ))
re = [[0] *(len(M)+1) for j in range(len(N)+1)]

for i in range(1, len(N)+1):
    for j in range(1, len(M)+1):
        if N[i-1] == M[j-1]:
            re[i][j] = re[i-1][j-1] + 1
        else:
            re[i][j] = max(re[i-1][j], re[i][j-1])

print(max(map(max,re)))
