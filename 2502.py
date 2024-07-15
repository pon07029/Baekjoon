li=[1]
def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
        li.append(a)
    return a

D, K = map(int, input().split())
fibo(D)
a, b = li[-2], li[-3]

# if D%2==0:
for i in range(1, 100000):
        if (K-i*b)%a==0:
            print(i)
            print((K-i*b)//a)
            break
# else:
#     for i in range(1, 100000):
#         if (K-i*a)%b==0:
#             print(i)
#             print((K-i*a)//b)
#             break
    