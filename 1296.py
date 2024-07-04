L, O, V, E = 0,0,0,0

def fun(q,w,e,r):
  return ((q+w)*(q+e)*(q+r)*(w+e)*(w+r)*(e+r))%100

li= []

b = input()
L = b.count("L")
O = b.count("O")
V = b.count("V")
E = b.count("E")
for i in range(int(input())):
  a = input()
  li.append([a, fun(a.count("L")+L,O+a.count("O"),V+a.count("V"),E+a.count("E"))])
li.sort(key=lambda x : (x[1], x[0]))
print(max(li, key=lambda x: x[1])[0])
 
