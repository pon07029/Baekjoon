N = list(map(int, input().split()))
M = input()
li=[]*len(N)
li.append([M.find(N[0])])
for i in range(1,len(N)):
    for j in li[i-1]:
        s = M.find(N[i], j[-1])
        if s != -1:
            li[i].append(j+[s])

    li[i].append(M.find(N[i]))
