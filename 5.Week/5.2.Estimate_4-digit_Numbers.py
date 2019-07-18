print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


chosen = 2587
chosen = list(str(chosen))              #sayimizi liste sekline getirip icinde daha rahat islem yapabiliriz

while True:
    plus = 0
    minus = 0
    estimate = input("Please, enter a four digit number to estimate without '0': ")
    if not estimate.isdigit():                  #eger sayi degilse uyari blogu
        print("Enter just numbers, please...")
    else:
        for i in range(len(chosen)):            #burda araligi olan integer olarak gostermelisin aksi halde hata verir
            if estimate[i] == chosen[i]:        #herhangi bir degere karsilik gelen indis dogruysa 1 arttir
                plus += 1
            elif estimate[i] in chosen:         #ayni deger var ama farkli yerdeyse 1 azalt
                minus -= 1
            else:
                print("Nothing same in the chosen number...JAMMER")     #hicbir sayi uymuyorsa for dan cik sonra normal devam et
                break
                continue
        if minus != 0 and plus != 0:            #bu if blogu for dongusunden cikmamizi hemde + - kontrolu sagliyor
            print('+', plus, ' ', minus)
        elif minus != 0:
            print(minus)
        elif plus != 0:
            print('+', plus, sep="")
        if plus == 4:                           #4 basamakta bilinirse
            print("Congratulations... Estimated number is {}".format(chosen))


#benzer sayi icinde bulunup fazla basamakli sayi girilmesi durumu eklenmedi!!!
#while dongusu cikisida eklenmedi istedigimiz kadar yapalim diye sorgu blogu koyulabilir EVET ;)