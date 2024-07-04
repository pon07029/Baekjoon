re =[]
while True:
    a = input()

    if a == "#":
        break
    re.append(a.count("a")+a.count("e")+a.count("i")+a.count("o")+a.count("u")+a.count("A")+a.count("E")+a.count("I")+a.count("O")+a.count("U"))

print(*re, sep="\n")