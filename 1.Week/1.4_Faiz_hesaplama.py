ana_para = int(input("Lutfen Ana Para Miktarini Giriniz: "))
faiz_suresi = int(input("Lutfen Suresini Yil Olarak Giriniz: "))
faiz_orani = int(input("Lutfen Faiz Oranini Yuzde Olarak Giriniz: "))

yillik_faiz_hesaplama = ana_para * faiz_suresi * faiz_orani / 100
aylik_faiz_hesaplama = ana_para * faiz_suresi * faiz_orani / (100*12)
gunluk_faiz_hesaplama = ana_para * faiz_suresi * faiz_orani / (100*12*30)

Toplam_faiz_miktari = ana_para + yillik_faiz_hesaplama

dosya = open("faizhesaplama.txt", "w")
print("Toplam para miktari", Toplam_faiz_miktari, "Euro'dur.", "\n", "Gunluk faiz miktari", gunluk_faiz_hesaplama, "Euro'dur. \n",
      "Aylik faiz miktari", aylik_faiz_hesaplama, "Euro'dur.", file=dosya)
dosya.close()
