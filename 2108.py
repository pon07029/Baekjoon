import math
import sys
a = int(input())
re=[]
dic={}
for i in range(a):
  b = int(sys.stdin.readline())
  re.append(b)
  if b in dic:
    dic[b]+=1
  else:
    dic[b]=1
re.sort()
# 딕셔너리의 값들만 추출
values = list(dic.values())
max_frequency = max(values)
# 최빈값 찾기 (빈도가 최대인 값들)
modes = [k for k, v in dic.items() if v == max_frequency]
modes.sort()
print(math.floor(sum(re)/len(re)+0.5))
print(re[(len(re)-1)//2])
print(modes[0] if len(modes)==1 else modes[1])
print(max(re)-min(re))
