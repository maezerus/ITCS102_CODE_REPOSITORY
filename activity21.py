sum = 0 

golang = True

while golang == True:
    x = int(input("Enter a number: "))

    if x == 0:
        print("Loop Terminated")
        print("Total of all numbers is",sum)
        break
    else:
        print("continue loop")
        sum += x
        print("current total is",sum)
        continue