a = 1000-int(input())
sum=0
for i in [500, 100, 50, 10, 5, 1]:
    sum+=a//i
    a%=i
print(sum)