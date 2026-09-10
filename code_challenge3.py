Sender Name = input("Name of sender? --->")
Type of Item = input("Type of Item? --->")
Is Fragile= bool(input("Is it fragile? (Enter \"yes\" if yes, press Enter if no) --->"))
weight = float(input("What's the weight of the object? (in kg) --->"))
is express = bool(input("distance "in km) ---->"))
is international = bool(input(is it international? (Enter \"yes\" if yes, press Enter if no))


#Calculating base cost

base cost = (weight * 2.5) * (distance * .15)

#Free shipping

if weight <= 2 and distance >= 100 and is express == False and is international == False
 	print("Free Shipping!!")
 	Total = 0


#International Express

elif is express == True and is express == True :
 	print("Package is International is applied")
 	Total = (base cost * 1.4) + 50

#Express or Heavy International

elif is express == True or (is_international == True and weight > 20) :
 	print("Package is Express or Heavy International is applied")
 	Total = (base_cost * 1.2) + 25

#Oversized

elif weight > 30 or distance > 1000 :
 	print("Oversized is aplied")
 	Total = base cost + 30

#Standard rate

else: 
 	Total = base_cost
 	print("Standard rate is applied")

print("--------------------------------------------------------")
print("Name of Sender", Sender Name)
print("Type of Item", Type of Item)
print("Total Output : PHP ", Total)