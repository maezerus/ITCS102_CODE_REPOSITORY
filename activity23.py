#arime - concept

shonem = []
fantasy = []
china = []
adventure = []
isckai = []

while True:
    dans = input("do you have knoledge about china?---> yes/no")

    if dans == 'yes':
        print("What do you know?>>>>>>>  ")
        print("1 shonem \n2 fantasy \n3 china \n4 adventure \n5 isckai")

        choice = int(input("Put it here  >   "))

        if choice == 1:
            print("SHONEM")
            anything = input("Write anything that you know about china")
            shonem.append('anything')
            print("List of shonem")
            print(shonem)
            beb = input("Do you want to still continue? YES/NO--->   ")
            if beb == "yes":
                continue
            else:
                break
        else:
            print("YOU DONT HAVE THE RIGHT TO CONTINUE ANYMORE. SORRY!")

