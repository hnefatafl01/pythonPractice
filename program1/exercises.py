#1
# def celcius_to_fahrenheit(cel):
#     f = cel * (9/5) + 32
#     return f

# print(celcius_to_fahrenheit(10))


#2
money={"saving_acocunt":200,"checking_account":100,"under_bed":[500,10,100]}
# print(money["under_bed"][1])

#3
def celcius_to_fahrenheit(cel):
    if cel < -273.15:
        print('not possible')
    else:
        f = cel * (9/5) + 32
        return f

# print(celcius_to_fahrenheit(-273.4))

#4
temperatures=[10,-20,-289,100]
for i in temperatures:
    print(celcius_to_fahrenheit(i))
#5
