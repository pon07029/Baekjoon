import math
li=[]
re =[]
tmp=[]

def sli(arr, n, k):
  j=0
  while k in arr :
    arr.remove(k)
    j+=1
  if len(arr)==0:
    return []
  # if n >= len(arr):
  #   return arr*math.ceil((n+1)/len(arr))
  tmpli =  arr[n-j:]+ arr[:n-j] 
  while n >= len(tmpli):
    tmpli+=tmpli[:a-len(re)]
  return tmpli 

a, b= map(int, input().split())
for i in range(a):
  li.append(i+1)

while len(re) < a:
  k=li.pop(b-1)
  re.append(k)
  li=sli(li, b-1, k)
  

formatted_string = ', '.join(map(str, re))
print(f'<{formatted_string}>')

