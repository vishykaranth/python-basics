import math

x = 2.9
print(round(x))
print(abs(-2.9))

# Math module
print(math.ceil(2.9))
print(math.floor(2.9))

#If Statements
# is_hot = True
is_hot = False
is_cold = False

if(is_hot):
    print("It's a hot day")
    print("Drink plenty of water")
elif(is_cold):
    print("Its a cold day")
    print("Wear warm cloths")
else:
    print("It's a lovely day")
print("Enjoy your day.")

price = 1000000
has_good_credit = False

if(has_good_credit):
    down_payment = (price * 10)/100;
else:
    down_payment = (price * 20)/100;

# print(F"Down Payment: ${down_payment}");

# Logical Operators
has_high_income = False
has_good_credit = True

if has_good_credit and has_high_income:
    print("Eligible for Loan-and")

if has_good_credit or has_high_income:
    print("Eligible for Loan-or")

has_criminal_record = True
if has_good_credit and not has_criminal_record:
    print("Eligible for Loan-and-not")



temperature = 30

if temperature == 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

name = "ab"
if len(name) < 3:
    print("Name must be atleast 3 char")
elif len(name) > 50:
    print("Name must be longer than 50 char")

