inputs = []

while True:
    x, y = map(int, input().split())

    if x == 0 and y == 0:
        break
    inputs.append("Yes" if x>y else "No")

for pair in inputs:
    print(pair)
