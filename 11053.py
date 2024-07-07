import sys
n= int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
are = [1]*n
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if arr[i] < arr[j]:
            are[i] = max(are[i], are[j]+1)
print(max(are))