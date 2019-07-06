print(14 * " >", "\t n.B.a. \t", "< " * 14)

chosen = 87
count = 0

while True:
    count += 1
    estimate = input("Please, enter one integer: ")
    try:                                                        # for ValueError giving
        estimate = int(estimate)
        for i in range(0, 100):                                 # how much times try giving
            if estimate == chosen:
                print(u"\U0001F31F", "Congratulations, number {} predicted ".format(chosen), count,
                      ". try is 'Success'", u"\U0001F31F", sep="")
                quit()                                                  #when is sucsess then quit
            elif estimate in range(chosen - 5, chosen) or estimate in range(chosen, chosen + 5):
                print(count, ". try is failure...YOU ARE VERY CLOSE...", sep="")
                break
            elif estimate in range(chosen - 10, chosen - 5) or estimate in range(chosen + 5, chosen + 10):
                print(count, ". try is failure...YOU ARE CLOSE...", sep="")
                break
            elif estimate in range(chosen - 20, chosen - 10) or estimate in range(chosen + 10, chosen + 20):
                print(count, ". try is failure...LITTLE BIT FAR...", sep="")
                break
            else:
                print(count,
                      ". try is failure...\n You predicted a very low or high number, you must enter a lower or higher number!...",
                      sep="")
                break

    except ValueError:
        print("Sorry, you can use only integers...Please try again!")
