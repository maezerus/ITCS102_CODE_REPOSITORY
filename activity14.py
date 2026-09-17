

# credit_score (integer)
# annual_income (float)
# has_collateral (boolean)

age = int(input("Enter your age --->"))
is_employed = bool(input("Are you currently employed? --->"))
credit_score = int(input("Enter your credit score --->"))
annual_income = float(input("How much is your annual income? --->"))
has_collateral = bool(input("Do you have any collateral (True / False) ---> "))

base_rate = 0.0

if age >= 21 and is_employed == True:
    print("Applicant passed baseline requirement")
    if credit_score >= 750: #tier1
        print("You have a high credit score!!")
        if annual_income >= 100000:
            base_rate = 4.5
            print("You have a high salary and high credit score, your interest rate is", base_rate)
        else: 
            base_rate = 5.0
            print("You have a high salary and high credit score, your interest rate is", base_rate)
    elif credit_score >= 600 and credit_score < 750:
        if has_collateral == True:
            base_rate = 7.0
            print("You have a high salary and high credit score, your interest rate is", base_rate")
    else: 
       print("Failed")

else:
    print("Rejected: Fails baseline criteria")

