# Distance_unit_conversion
# As you want to select unit 'km' or 'mil' then give variable and finally solve it.


unit = input("Please select the unit you want to convert as 'km' or 'mil': ")

if bool(unit) == True:
    if unit == "km":
        a = float(input("Please, enter the quantity you would like to calculate: "))
        b = a / (1.609344)
        print(a, "km is", b, "mil.")
    elif unit == "mil":
        b = float(input("Please, enter the quantity you would like to calculate: "))
        a = b * (1.609344)
        print(b, "mil is", a, "km.")
    else:
        print("Please, enter valid characters... ")
else:
    print("Please just enter 'km' or 'mil'...")


