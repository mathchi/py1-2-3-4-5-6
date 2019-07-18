print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

pics = ["""
   +---+
   |   |
       |
       |
       |
       |
--------""", """
   +---+
   |   |
   O   |
       |
       |
       |
--------""", """
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\  |
       |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
--------""", """
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
--------"""]

count1 = 6              #kac hakki oldugunu belirttik
count2 = 0              #resimleri sirasiyla versin diye sayac
word = "karpuz"

print("Welcome to my HANG MAN play. You have {} rights. Let's start... ".format(count1))

under_score = list()                #alt tire liste olusturma

for i in range(len(word)):          #alt tire olusturma miktari ve yazdirma
    under_score.append("_")

while under_score.count("_") > 0:

    print(pics[count2])             #resim atandi ve yazdirildi
    print(under_score)              #alt tire yazdirma

    letter = input("Please enter one letter: ").lower()
    if letter.isalpha():                #girilen sey harf degilse sarti koyuldu
        if letter not in word:
            count1 -= 1                 #yanlis harf girisinde hakki dusmesi icin
            count2 += 1                 #sonraki resim gelsin diye
            if count1 <= 0:
                print(pics[6])          #enson resim
                print("Unfortunately you lost...")
                exit()
        else:
            for i in range(len(word)):          #kelime boyunca harf arama
                if letter == word[i]:           #eger harf kelimenin ogesi ise
                    under_score[i] = letter     #kelimenin ogesi olan harf oraya atansin

        print(under_score)
    else:
        print("You cannot enter anything other than 'letter'!!!")
print("Congragulations...")





#BURASI EGER DIREKT KELIME GIRMEK ICIN EKSTRA KOYULABILIR!
# wol = int(input("Kelime veya harf icin 1 veya 2 giriniz: "))
#     if wol == 1:
#         kullanici_tahmin = input("Kelime tahmini girin: ").lower()
#         if kullanici_tahmin == word:
#             print("Kazandiniz!!!", word)
#             exit()
#         else:
#             tahminikelime.append(kullanici_tahmin)
#             count2 += 1
#             print("Yanlis tahmin!", 6-count, "hakkiniz kaldi.")
#             break
