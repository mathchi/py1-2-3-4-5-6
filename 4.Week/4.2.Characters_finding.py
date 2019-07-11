print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


while True:
    sentence = input("Please write the sentence you want to do: ")
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    if sentence:
        for say in sentence:                            #cumledeki her bir karakteri tarasin
            if say.isupper():                           #taranan her bir karakterde buyuk harf varmidir?
                count1 += 1                             #sayacimiz her gordugunde sayisini birer arttiracak

            elif say.islower():                         #taranan her bir karakterde kucuk harf varmidir?
                count2 += 1

            elif say.isdigit():
                count3 += 1

            else:                                       #geriye sadece ozel karakter sayimi kaliyor
                count4 += 1

        print("There are(is) a total of {} letter(s) in your sentence.".format(count1 + count2))
        print("{} of them uppercase,".format(count1))
        print("{} of them lowercase.".format(count2))
        print("There are(is) {} numbers and {} has special character(s).".format(count3, count4))
        break
    else:
        print("You have to write somethings...Please try again!")
