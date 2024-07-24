x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())


a= (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
b= (x2-x1)*(y4-y1)-(y2-y1)*(x4-x1)
c= (x4-x3)*(y1-y3)-(y4-y3)*(x1-x3)
d= (x4-x3)*(y2-y3)-(y4-y3)*(x2-x3)
# print(a,b)
# print(c,d)
if a==0 and b==0:
    if x1<=x3<=x2 or x2<=x3<=x1:
        if y1<=y3<=y2 or y2<=y3<=y1:
            print(1)
            exit()
    if x1<=x4<=x2 or x2<=x4<=x1:
        if y1<=y4<=y2 or y2<=y4<=y1:
            print(1)
            exit()
    if x3<=x1<=x4 or x4<=x1<=x3:
        if y3<=y1<=y4 or y4<=y1<=y3:
            print(1)
            exit()
    if x3<=x2<=x4 or x4<=x2<=x3:
        if y3<=y2<=y4 or y4<=y2<=y3:
            print(1)
            exit()
    print(0)
    exit()
else:
    if a*b<=0 and c*d<=0:
        print(1)
        exit()
    print(0)
    exit()