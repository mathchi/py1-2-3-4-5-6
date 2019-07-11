print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

dimension = """Select:                      

1 = Letter 'CAPITALIZED'
2 = Letter 'minimized'

"""
print(dimension)                    #NE YAPACAGINA DAIR SECIM YAPMAK ICIN

while True:                         #DONGU HALINDE ALALIM KI DAHA COK YAPMAK ISTENIRSE DIYE
    select = input("Please enter the process you want to do: ")

    try:
        select = int(select)           #INTEGER SECMEDIGINDE HATA VERSIN
        if select not in range(1,3):            #SECIM ARALIGI ICINDE DEILSE
            print("Please enter for process just 1 or 2 numbers... Try again!")
        else:
            sentence = input("Please write the sentence you want to convert: ")
            if (select == 1):
                print(sentence.upper())
                yesno = input("If you want to continue enter YES = 'Y' or NO = 'N': ")
                print(yesno)
                if yesno == "E":                #YAPMAYA DEVAM ETMEK ISTENIRSE DIYE EKLENDI
                    continue
                elif yesno == "N":                           #AKSI HALDE CIKIS
                    break
                else:
                    print("Please enter correct letter (Y/N)...")
            elif (select == 2):
                print(sentence.lower())
                yesno = input("If you want to continue enter YES = 'Y' or NO = 'N': ")
                print(yesno)
                if yesno == "E":
                    continue
                elif yesno == "N":                               # AKSI HALDE CIKIS
                    break
                else:
                    print("Please enter correct letter (Y/N)...")
    except ValueError:
        print("You entered a value error... Please try again!")


