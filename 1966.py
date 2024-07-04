def fun(l, n):
  lis=l
  now=n
  tmp=1
  while True:
    if max(lis) == lis[0]:
      if now==0:
        return tmp
      else:
        lis.pop(0)
        tmp+=1
        now-=1
    else:
      if now==0:
        now=len(lis)-1
        k = lis.pop(0)
        lis = lis +[k]
      else:
        k = lis.pop(0)
        lis = lis +[k]
        now-=1

a = int(input())
re=[]
for i in range(a):
  b, c = map(int, input().split())
  dat = list(map(int, input().split()))

  re.append(fun(dat,c))

for i in re:
  print(i)