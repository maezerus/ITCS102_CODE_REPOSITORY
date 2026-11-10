deck = int(input("Enter size:  "))

for a in range(deck):
    for b in range(deck - a - 1):
        print(" ", end= " ")

    for c in range(deck):
        if a == 0 or a == deck - 1 or c == 0 or c == deck - 1:
            print("*", end= " ")
        else:
            print(" ", end= " ")
    print( )