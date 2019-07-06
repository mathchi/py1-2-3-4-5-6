print(14*" >", "\t n.B.a. \t", "< "*14)

while True:
    number = input("Please enter one number: ")
    if not number:                                              #could not pass without number
        print("You can not pass without enter!")
    else:
        try:
            number = int(number)
            if number > 1:                                      #prime number should be > 1
                for divided in range(2, number//2+1):             #restricted until entering number
                    if (number % divided) == 0:                   #divided until itself
                        print(number, " is NOT a Prime Number.\n", divided, " times ", number // divided, " is ", number,".", sep="")
                        break
                else:
                    print(number, "is a Prime Number!")
                    break
            else:
                print(number, "is not a Prime Number.")

        except ValueError:
            print("Sorry, you can use only integers...Please try again!")
    break

