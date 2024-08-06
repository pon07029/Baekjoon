
def sl(num, n):
    l=len(str(num))
    if l>n:
        return int(str(num)[l-n:])
    return num

def f(b,i,n):
    if i==0:
        return 1
    return sl(b**f(b,i-1,n),n)
    # if i%2==0:
    #     return sl(f(b,i//2,n)**2,n)
    # return sl(f(b,i-1,n)*b,n)

print(f(10,10,6))