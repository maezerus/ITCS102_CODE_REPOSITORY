
#JEEPNEY SIMULATOR (interactive)

route = ["Terminal", "Perez Park", "Pacific Mall"]
passenger = [ ]
SEATS = 6
FARE = 13
total = 0

while True:
    print()
    print(len(passenger), "of", SEATS, "seats")
    print("1 sakay \n2 priority seats \n3 para po!!!")
    print("4 baba sa pinto \n5 baba sa harap")
    print("6 seat check \n7 balikan \n8 exit")
    choice = input("choice:  ")

    if choice == "1":
        if len(passenger) == SEATS:
            print("wala na po, puno na!")
        else:
            name = input("name:   " )
            passenger.append(name)
            total = total + FARE 
            print(name, "boarded at the back.")

    elif choice == "2":
        if len(passenger) == SEATS:
            print("PUNO NA NGANI")
        else:
            name = input("name:   " )
            passenger.insert(0, name)
            total = total + FARE 
            print(name, "took the priority seat.")

    elif choice == "3":
            name = input("sino pong bababa?")
            if name in passenger:
                passenger.remove(name)
                print(name, "baba na po. INGATTT")
            else:
                print(name, "is not on this jeep.")

    elif choice == "4":
            if len(passenger) == 0:  
                print(name, "ubos na ang aking pasahero :<")
            else:
                left = passenger.pop( )
                print(left, "got off at the door.")

    elif choice == "5":
                if len(passenger) == 0:  
                    print(name, "ubos na ang aking pasahero :<")
                else:
                    front = passenger.pop(0)
                    print(front, "got off at the front.")

    elif choice == "6":
         for i in range(len(passenger)):
              print("Seat", i + 1, passenger[i])

    elif choice == "7":
         route.reverse()
         print("Route: ", route)

    elif choice == "8":
            print("Total fare today:", total)
            break
    else:
         print("invalid choice.")
            