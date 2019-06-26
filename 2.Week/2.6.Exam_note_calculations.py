# Total note >= 90 -----> AA
# Total note >= 85 -----> BA
# Total note >= 80 -----> BB
# Total note >= 75 -----> CB
# Total note >= 70 -----> CC
# Total note >= 65 -----> DC
# Total note >= 60 -----> DD
# Total note >= 55 -----> FD
# Total note < 55 -----> FF

visa1 = input("Please enter 1.visa note: ")
visa2 = input("Please enter 2.visa note: ")
final = input("Please enter final note: ")

if bool(visa1) == True and bool(visa2) == True and bool(final) == True:
    visa1 = int(visa1)
    visa2 = int(visa2)
    final = int(final)
    averaga_note = float((visa1 + visa2) * 0.3 + final * 0.4)
    if visa1 > 100 or visa1 < 0 or visa2 > 100 or visa2 < 0 or final > 100 or final < 0:
        print("You can not enter greater than 100 point...")
    elif averaga_note >= 90:
        print("Your average note is", averaga_note, "and letter is 'AA'.")
    elif averaga_note >= 85:
        print("Your average note is", averaga_note, "and letter is 'BA'.")
    elif averaga_note >= 80:
        print("Your average note is", averaga_note, "and letter is 'BB'.")
    elif averaga_note >= 75:
        print("Your average note is", averaga_note, "and letter is 'CB'.")
    elif averaga_note >= 70:
        print("Your average note is", averaga_note, "and letter is 'CC'.")
    elif averaga_note >= 65:
        print("Your average note is", averaga_note, "and letter is 'DC'.")
    elif averaga_note >= 60:
        print("Your average note is", averaga_note, "and letter is 'DD'.")
    elif averaga_note >= 55:
        print("Your average note is", averaga_note, "and letter is 'FD'.")
    elif averaga_note < 55:
        print("Your average note is", averaga_note, "and letter is 'FF'.\n"
                                                    "You have to take this lesson again...")

    else:
        print("Please, try again with good characters.")
else:
    print("Please enter numbers... Try again. ")
