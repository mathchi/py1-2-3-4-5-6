# Password character control

username = input("Please, enter an user name between 3-18 characters: ")

# charecters = """ "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """
# numbers = [0,1,2,3,4,5,6,7,8,9]

if (bool(username) == True):

    if ("1" in username) or ("2" in username) or ("3" in username) or ("4" in username) or ("5" in username) \
            or ("6" in username) or ("7" in username) or ("8" in username) or ("9" in username) or ("0" in username):
        print("You cannot use numbers in the User name. Please try again...")
    else:
        if 3 <= len(username) <= 18:
            password = input("Please, enter a password between 6-12 characters: ")
            if 6 <= len(password) <= 12:
                dosya = open("passcontrol.txt", "w")
                print("Your User Name : ", username, "\n",
                      "Your Password : ", password, file=dosya)
                dosya.close()
            elif len(password) < 6 or len(password) > 12:
                print("Password should be between 6-12 characters. Please try again... ")
        elif len(username) < 3 or len(username) > 18:
            print("User name should be between 3-18 characters. Please try again...")

else:
    print("Please enter at least 3 letter for User Name... Try again. ")

