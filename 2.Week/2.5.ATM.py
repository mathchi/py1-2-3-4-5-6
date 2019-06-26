#Money process in the ATM

balance = 1000

enter = """Welcome to homepage...
(1) Balance control
(2) To deposit money
(3) Make a draft money
(4) Homepage
"""
print(enter)
question = input("Please, select the action what do you want to do: ")
if question == "1":
    print("Your balance", balance, u"\u20AC")
    home = input("""If you want to back Homepage press 4, 
    If you want to exit press Exit: """)
    if home == "4":
        enter = """Welcome to homepage...
        (1) Balance control
        (2) To deposit money
        (3) Make a draft money
        (4) Homepage
        """
        print(enter)
        question = input("Please, select the action what do you want to do: ")
    # Burda Homepage dondukten sonra secenekler arttirilabilir.
    elif home == "exit":
        print("See you again HAVE A NICE DAY...")
    else:
        print("You pressed the wrong button EXITING...")

elif question == "2":
    deposit = int(input("Enter how much you want to deposit: "))
    if deposit > balance:
        print("You cannot load more than your balance...")
    elif deposit % 10 == 0:
        print("To loading", deposit, u"\u20AC", "\nDo you confirm? \nPress Yes or Press Exit" )
    #Secenek arttirilabilir.
    elif deposit % 10 != 0:
        print("Just you can load 10 and multiples 10...")

elif question == "3":
    draft = int(input("How much money you want to do: "))
    if draft > balance:
        print("You can not withdraw more than your balance...")
    elif draft <= balance:
        print(draft, u"\u20AC", "will be withdrawn from your account. Please, Don't forget your card...")
else:
    print("""You didn't select between 1 - 3. 
          If you don't want to do anything 
          press Exit... """)
