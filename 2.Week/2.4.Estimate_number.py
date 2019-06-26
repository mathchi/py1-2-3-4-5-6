# Estimate number play

chosen = input("Please, chose one number between 1 to 10: ")
estimate = input("Please, estimate one number between 1 to 10: ")

if bool(chosen) == True and bool(estimate) == True:
    estimate = int(estimate)
    chosen = int(chosen)
    if estimate == chosen and 1 <= estimate < 10 and 1 <= chosen < 10:
        print(3 * u"\U0001F31F", "'PERFECT' First try is 'SUCCESSFUL'", 3 * u"\U0001F31F")
    elif estimate != chosen:
        print("First try is failure...")
        est1 = int(input("Please, estimate one number between 1 to 10: "))
        if est1 == chosen:
            print(2 * u"\U0001F31F", "VERY GOOD Second try is 'SUCCESSFUL'", 2 * u"\U0001F31F")
        elif est1 != chosen:
            print("Second try is failure...")
            est2 = int(input("Please, estimate one number between 1 to 10: "))
            if est2 == chosen:
                print(u"\U0001F31F", "GOOD Third try is 'SUCCESSFUL'", u"\U0001F31F")
            elif est2 != chosen:
                print("Third try is failure...")
                est3 = int(input("Please, estimate one number between 1 to 10: "))
                if est3 == chosen:
                    print(2 * u"\U0001F31F", "Congratulations Fourth try is 'Success'", 2 * u"\U0001F31F")
                elif est3 != chosen:
                    print("Fourth try is failure...")
                    est4 = int(input("Please, estimate one number between 1 to 10: "))
                    if est4 == chosen:
                        print(u"\U0001F31F", "Congratulations Fifth try is 'Success'", u"\U0001F31F")
                    elif est4 != chosen:
                        print("and fifth try is completely 'FAILURE'. \n You can't log in more...")
    else:
        print("Please, enter one number between 1 to 10...")
else:
    print("Please enter one number between 1 to 10... Try again.")
