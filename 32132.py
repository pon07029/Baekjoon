N=int(input())
w=input()

while "PS5" in w or "PS4" in w:
    w=w.replace("PS5","PS")
    w=w.replace("PS4","PS")
print(w)