a, b= map(int, input().split())

for i in range(2, b+1):
    if i==b:
        print("GOOD")
        break
    if a%i==0:
        print(f"BAD {i}")
        break
