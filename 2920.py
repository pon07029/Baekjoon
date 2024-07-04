dat = list(map(int, input().split()))

if dat == sorted(dat):
  print("ascending")
elif dat == sorted(dat, reverse = True):
  print("descending")
else:
  print("mixed")