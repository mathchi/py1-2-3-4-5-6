print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

source = "şçöğüıŞÇÖĞÜİýãÞÝþäŠðèéš"          #Ceviri yapilmasini istedigimiz harfler
aim = "scoguiSCOGUIiasIsaSgees"             #cevirilecek harflerle esit sayida olmali

with open("futbolcular.txt", "r", encoding="cp1254") as ikra1:
    file = ikra1.read()                       #dosyamizi okutuyoruz

with open("English_translated.txt", "w+", encoding="cp1254") as ikra2:
    file1 = str.maketrans(source, aim)      #ceviri yapma fonksiyonu
    file2 = file.translate(file1)           #burasi print yerine kolay yazilsin diye verdik
    ikra2.write(file2)                      #acmis oldugumuz dosyayi yazdiriyoruz
    print(file2)