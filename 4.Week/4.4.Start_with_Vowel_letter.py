print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

bass = ('a','e','i','o','u')                #startswith kullanmak icin kelimeler tuple olmali

with open("futbolcular.txt", "r", encoding="cp1254") as ikra:    #okuma modunda ac
    file = ikra.readlines()                                     #kelime kelime okutuyoruz
    #file = ikra.read().split("\n")           read olarak okutacaksak buda alternatif sekil

with open("startvowel.txt", "w+", encoding="cp1254") as ikra2:       #yazdirmamiz gereken dosyayi acalim
    for letter in file:                                      #okuttugumuz dosyadaki harfleri tektek taramak icin for
        if letter.lower().startswith(bass):                 #ilk bastaki harf eger buyuk olursa diye lower sonrasinda startswith
            print(letter)                                   #secilen satirlari ekrana yazdir
            ikra2.write(letter)                             #ismini verdigimiz dosyaya yaz