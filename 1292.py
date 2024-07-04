li =[i for i in range(1, 50 + 1) for _ in range(i)]
sum = 0
a, b= map(int, input().split())

for i in range(a-1, b):
    sum+=li[i]
print(sum)