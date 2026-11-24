def taga_triangle(number):
    for x in range(number, 0, -1):
        for y in range(1, x+1):
            print("*", end=" ")
        print( )

def sum(x, y):
    return x+y


def box(size):
    for x in range(size+1):
        for y in range(size+1):
            if y == 0 or x == 0 or x == size or y == size:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print( )


def my_factorial(number):
    fact = 1
    for x in range(number, 0, -1):
        fact *= x
    return fact

# box(6)
# box(10)

# taga_triangle(3)
# taga_triangle(24)
# taga_triangle(17)
# taga_triangle(20)

# print(sum(30, 24))
# print(sum(15, 4) * 2000)