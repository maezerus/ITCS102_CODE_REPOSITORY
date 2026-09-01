money = input("Enter amount to deposit")
print("=========== PH PESO DENOMINATION BREAK DOWN =============")
print("CURRENT MONEY IS =====>", money)
libo = money // 1000 #935 -> how to brimg down this value 8.935
libo_sukli = money % 1000 # 935
five_h = libo_sukli // 500
five_sukli = money % 1000 # 935
two_h = libo_sukli // 200 
two_sukli = money % 1000 # 935
one_h = libo_sukli // 100
one_sukli = money % 1000 # 935
fifty = libo_sukli // 50
fifty_sukli = money % 1000 
twenty = libo_sukli // 20
twenty_sukli = money % 1000
five  = libo_sukli // 5
five_sukli = money % 1000
one = libo_sukli // 1
one_sukli = money % 1000

print("1000 - ",)
print("500 - ",)
print("200 - ",)
print("100 - ",)
print("50 - ",)
print("20 - ",)
print("10 - ",)
print("5 - ",)
print("1 - ",)
print("=========================================================")
