shape = """ Chose one number
(1) triangle
(2) quadrangle
"""
print(shape)

chosen = input("Please, which shape do you want to choose: ")
if chosen == "1":
    first_edge = abs(int(input("Enter first edge: ")))
    second_edge = abs(int(input("Enter second edge: ")))
    third_edge = abs(int(input("Enter third edge: ")))
    if first_edge == second_edge == third_edge:
        print("This is 'EQUILATERAL TRIANGLE'.")
    elif first_edge == second_edge and first_edge != third_edge:
        print("This is 'ISOSCELES TRIANGLE'.")
    elif first_edge != second_edge != third_edge:
        print("This is 'TRIANGLE'.")
    else:
        print("This is not Triangle!!!")

elif chosen == "2":
    first_edge = abs(int(input("Enter first edge: ")))
    second_edge = abs(int(input("Enter second edge: ")))
    third_edge = abs(int(input("Enter third edge: ")))
    fourth_edge = abs(int(input("Enter fourth edge: ")))
    if first_edge == second_edge == third_edge == fourth_edge:
        print("This is 'SQUARE'.")
    elif first_edge == third_edge and second_edge == fourth_edge:
        print("This is 'RECTANGULAR'")
    else:
        print("This is 'QUADRANGLE'.")

else:
    print("Sorry, this can not give any shape...")