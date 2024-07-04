a, b= map(str, input().split())
a =list(a)
a.reverse()

for i in range(len(a)):
    if ord(a[i]) >= 65:
        a[i] = ord(a[i])-55
    else:
        a[i] = int(a[i])
for i in range(len(a)):
    a[i] = a[i]*(int(b)**i)
print(sum(a))