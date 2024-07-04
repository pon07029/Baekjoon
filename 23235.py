a =0
while True:
    dat = list(map(int, input().split()))

    if dat[0]== 0:
        break
    a+=1

for i in range(a):
  print(f"Case {i+1}: Sorting... done!")