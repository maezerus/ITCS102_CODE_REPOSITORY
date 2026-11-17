teh = int(input("Enter number of column---> "))

for x in range(1, 11):
    for y in range(1, teh + 1):
        print(x,"x",y,"=",x*y, end="\t")
    print( )
