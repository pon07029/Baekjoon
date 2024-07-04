a, b= map(int, input().split())
dat = list(map(int, input().split()))

for i in dat:
    print(i-a*b, end=' ')