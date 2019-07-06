print(14 * " >", "\t n.B.a. \t", "< " * 14)

select = """\t Please select one of following numbers...
 1 - Account created
 2 - Exit			
"""
print(select)

while True:
    try:                                                        #for value error
        command = input("Please enter numbers '1' or '2': ")
        if command == "1":
            with open("registration.txt", "r+") as file:        #open and read file
                nickname = input("Please enter username: ")
                ikra = file.readlines()
                for s in ikra:                                  #separate all columns and read words
                    if s == (nickname + "\n"):                  #if there is same name give me error
                        print("Now this username is using! Please enter another one...")
                        break
                else:                                           #if not same name then write in file
                    password = input("Please enter password: ")
                    file.write(nickname + "\n")
                    print("Your account created...")
                    break
        elif command == "2":
            print("Exiting...")
            break
        else:
            print("This is not acceptable...\n", select)
    except ValueError:
        print("Ooops...You cannot use integer in the User name. Please try again!")
