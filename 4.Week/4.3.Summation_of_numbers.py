print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


while True:
    sentence = input("Please write the sentence you want to do: ")
    count = 0
    Summation = 0
    if sentence:
        for ikra in sentence:
            if ikra.isdigit():
                count += 1
                Summation += int(ikra)
        print("There is(are) {} number(s) and sumaation of number(s) is {}.".format(count, Summation))
        break
    else:
        print("You have to write somethings...Please try again!")