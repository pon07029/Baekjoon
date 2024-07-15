p ={
    1: [2, 4],
    2: [1, 3, 5],
    3: [2, 6],
    4: [1, 5, 7],
    5: [2, 4, 6, 8],
    6: [3, 5, 9],
    7: [4, 8,0],
    8: [5, 7, 9],
    9: [6, 8],
    0: [7]
}
li =[[1,1,1,1,1,1,1,1,1,1]]
re=[]
for i in range(int(input())):
   re.append(int(input()))

for i in range(1,max(re)+1):
    tmp=[]
    for j in range(10):
         s=0
         for k in p[j]:
              s+=li[i-1][k]
         tmp.append(s)
    li.append(tmp)
for i in re:
    print(sum(li[i-1])%1234567)
   