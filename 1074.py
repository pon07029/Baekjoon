def fun(x,y, n):
    xtmp = x
    ytmp = y
    tmp =0
    if x>=2**(n-1):
        xtmp-=2**(n-1)
        tmp+=2
    if y>=2**(n-1):
        ytmp-=2**(n-1)
        tmp+=1

    return [xtmp, ytmp, n-1, tmp*(2**(n-1))*(2**(n-1)),tmp]

a, b, c= map(int, input().split())
re = 0
while a>0:
  k= fun(b,c,a)

  b =k[0]
  c=k[1]
  a=k[2]
  re=re+k[3]
if b==1:
  re+=1
if c==1:
  re+=2
print(re)