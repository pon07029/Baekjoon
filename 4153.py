inputs = []

while True:
    x, y, z = map(int, input().split())

    if x == 0 and y == 0 and z== 0:
        break
    da = [x,y,z]
    da.sort()
    inputs.append("right" if da[0]*da[0]+da[1]*da[1]==da[2]*da[2] else "wrong")

for i in inputs:
  print(i)