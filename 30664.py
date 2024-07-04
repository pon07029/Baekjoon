while True:
    a = int(input())

    if a==0:
        break
    print("PREMIADO" if a&42==0 else "TENTE NOVAMENTE")