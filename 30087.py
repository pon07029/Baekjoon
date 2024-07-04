a = int(input())
re=[]
for i in range(a):
  b = input()
  if b == "Algorithm":
    re.append("204")
  elif b == "DataAnalysis":
    re.append("207")
  elif b == "ArtificialIntelligence":
    re.append("302")
  elif b == "CyberSecurity":
    re.append("B101")
  elif b == "Network":
    re.append("303")
  elif b == "Startup":
    re.append("501")
  else:
    re.append("105")

for i in re:
  print(i)