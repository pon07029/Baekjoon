p ={
    1: [0, 2],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4, 6],
    6: [5,7],
    7: [6,8],
    8: [7, 9],
    9: [8],
    0: [1]
}
li =[[0,1,1,1,1,1,1,1,1,1]]
re=[]

for i in range(1,int(input())):
    tmp=[]
    for j in range(10):
         s=0
         for k in p[j]:
              s+=li[i-1][k]
         tmp.append(s)
    li.append(tmp)

print(sum(li[-1])%1000000000)
   