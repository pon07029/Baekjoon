A= input()
B= input()
li = [[""] * (len(B) + 1) for _ in range(len(A) + 1)]

for i in range(1,len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            li[i][j] = li[i-1][j-1] + A[i-1]
        else:
            if len(li[i-1][j]) >= len(li[i][j-1]):
                li[i][j] = li[i-1][j]
            else:
                li[i][j] = li[i][j-1]

if len(li[-1][-1]) == 0:
    print(0)
else:
    print(len(li[-1][-1]))
    print(li[-1][-1])
        
    
