aylik_gelir = int(input("Lutfen aylik geliri giriniz: "))
mutfak_harcama = int(input("Lutfen harcanan mutfak masrafini giriniz: "))
egitim_harcama = int(input("Lutfen harcanan egitim masrafini giriniz: "))
giyim_harcama = int(input("Lutfen harcanan giyim masrafini giriniz: "))
ulasim_harcama = int(input("Lutfen harcanan ulasim masrafini giriniz: "))

Aylik_toplam_harcama = mutfak_harcama + egitim_harcama + giyim_harcama + ulasim_harcama

Aylik_masraf_gelir_orani = Aylik_toplam_harcama / aylik_gelir

dosya= open("aylikmasraf.txt", "w")
print("Aylik toplam masraf", Aylik_toplam_harcama, "Euro'dur.", "\n",
"Aylik harcanan miktarin aylik gelire orani ", Aylik_masraf_gelir_orani, "Euro'dur", file=dosya)

dosya.close()