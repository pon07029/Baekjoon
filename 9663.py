N = int(input())
ch =[-2]*N
def check(l):
   
    for j in range(l):
        if abs(ch[j]-ch[l])==abs(j-l) or ch[l]==ch[j]:
            return False
    return True

def self(y):
    if y==0:
        return 1
    else:
        su=0
        for i in range(N):
            ch[N-y]=i
            if check(N-y):
                su+=self(y-1)
        return su
s=0
for i in range(N//2):
    ch[0]=i
    s+=self(N-1)*2
if N%2==1:
    ch[0]=N//2
    s+=self(N-1)
print(s)

