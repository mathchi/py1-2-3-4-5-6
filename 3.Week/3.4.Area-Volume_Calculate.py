print(14*" >", "\t n.B.a. \t", "< "*14)

import math

while True:
    shape = """ Chose following number
    (1) triangle (Area)
    (2) quadrangle (Area)
    (3) square (Area)
    (4) cube (Volume)
    (5) sphere (Volume)
    (6) cone (Volume)
    """
    print(shape)

    chosen = input("Please, which shape do you want to choose: ")
    try:
        if chosen == "1":
            first_edge = abs(float(input("Enter first edge: ")))
            second_edge = abs(float(input("Enter second edge: ")))
            third_edge = abs(float(input("Enter third edge: ")))
            h_height = abs(float(input("Enter height for triangle: ")))
            if first_edge == second_edge == third_edge:
                base1 = first_edge
                equil_tri_area = (base1 * h_height)/2
                print("This is an 'EQUILATERAL TRIANGLE'. Equilateral Triangle Area = ", equil_tri_area)
                break
            elif first_edge == second_edge and first_edge != third_edge:
                base2 = third_edge
                isos_area = (third_edge * h_height)/2
                print("This is an 'ISOSCELES TRIANGLE'. Isosceles Triangle Area = ", isos_area)
                break
            elif first_edge != second_edge != third_edge:
                base3 = second_edge
                triangle_area = (second_edge * h_height)/2
                print("This is a 'TRIANGLE'. Triangle Area = ", triangle_area)
                break
            else:
                print("This is not a Triangle!!!\n Please try again...")

        elif chosen == "2":
            first_edge = abs(float(input("Enter first edge: ")))
            second_edge = abs(float(input("Enter second edge: ")))
            third_edge = abs(float(input("Enter third edge: ")))
            fourth_edge = abs(float(input("Enter fourth edge: ")))
            h_height = abs(float(input("Enter height for quadrangle: ")))
            if first_edge == third_edge and second_edge == fourth_edge:
                rectangular_area = first_edge * second_edge
                print("This is a 'RECTANGULAR'. Rectangular Area = ", rectangular_area)
                break
            elif first_edge != second_edge != third_edge != fourth_edge:
                base4 = fourth_edge
                quad_area = h_height * base4
                print("This is a 'QUADRANGLE'. Quadrangle Area = ", quad_area)
                break

        elif chosen == "3":
            square_edge = abs(float(input("Enter edge: ")))
            square_area = square_edge**2
            print("This is a 'SQUARE'. Square Area = ", square_area)
            break

        elif chosen == "4":
            cube_edge = abs(float(input("Enter edge: ")))
            cube_volume = cube_edge ** 3
            print("This is a 'CUBE'. Cube Volume = ", cube_volume)
            break

        elif chosen == "5":
            radius = abs(float(input("Enter radius: ")))
            sphere_volume = 4 * (math.pi * (radius**3))/3
            print("This is a 'SPHERE'. Sphere Volume = ", sphere_volume)
            break

        elif chosen == "6":
            radius = abs(float(input("Enter radius: ")))
            height = abs(float(input("Enter height: ")))
            cone_volume = (math.pi * (radius ** 2) * height) / 3
            print("This is a 'CONE'. Cone Volume = ", cone_volume)
            break

        else:
            print("Sorry, this can not give any shape...Please try again!")
    except ValueError:
        print("Sorry!\n You have to use only numbers...")
