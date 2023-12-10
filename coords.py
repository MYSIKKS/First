def coords():
    x = int(input("Введите X "))
    y = int(input("Введите Y "))

    if (y > 0 and x > 0):
        print("I")

    if (y > 0 and x < 0):
        print("II")

    if (y < 0 and x < 0):
        print("III")

    if (y < 0 and x > 0):
        print("IV")
coords()