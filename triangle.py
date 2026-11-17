for x in range(6, 0, -1):
    for y in range(1, x+1):
        print("-", end=" ")
    for d in range(1, 7 - x):
        print(d, end=" ")
    for j in range(5-x, 0, -1):
        print(j, end=" ")
    print( )