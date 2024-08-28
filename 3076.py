R, C=map(int,input().split())
A, B = map(int,input().split())
for i in range(R):
    for _ in range(A):
        t=""
        for j in range(C):
            if (i+j)%2==0:
                t+="X"*B
            else:
                t+="."*B
        print(t)
