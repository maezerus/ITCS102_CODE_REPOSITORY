from activity25 import taga_triangle
from activity25 import box
from activity25 import sum
from activity25 import my_factorial
import os

while True:
    print("MIMI MENU")
    print("SELECT AN OPTION")
    print("1 - Triangle")
    print("2 - SUM")
    print("3 - Box")
    print("4 - Factorial")
    print("5 - EXIT")
    choose = int(input("Which option to go? ---->  "))

    if choose == 1:
        os.system("cls")
        print("TAGA TRIANGLE")
        size = int(input("SIZE NG TRIANGLE ---> "))
        taga_triangle(size)
        continue

    elif choose == 2:
        print("SIMPLE SUMMATION")
        num1 = int(input("number 1 --> "))
        num2 = int(input("number 2 --> "))
        print(f"the sum of {num1} and {num2} is{sum(num1, num2)}")
        continue

    elif choose == 3:
            print("BOX")
            size = int(input("INPUT ANY NUMBER ---> "))
            box(size)
            continue

    elif choose == 4:
            print("FACTORIAL")
            num = int(input("input any number ---> "))
            print(f"the Factorial of {num} and is {my_factorial (num)}")
            continue

    elif choose == 5:
          print("SYSTEM EXIT")
          break
    else:
          print("INVALID CHOICE!")
          continue
    




    
        