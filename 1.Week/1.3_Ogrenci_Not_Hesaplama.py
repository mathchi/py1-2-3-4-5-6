ad = input("Lutfen adi giriniz: ")
soyad = input("Lutfen soyadi giriniz: ")
vize = int(input("Lutfen vize notunu giriniz: "))
final = int(input("Lutfen final notunu giriniz: "))
girilenders = int(input("Lutfen kacirdigi ders miktarini giriniz: "))
ders_takip =100-(girilenders * 5)

vize_orani = vize * 0.3
final_orani = final * 0.5
derstakip_orani = ders_takip * 0.2
Ogrenci_yil_sonu_notu = vize_orani + final_orani + derstakip_orani

dosya = open("ogrenciNotHesaplama.txt", "w")

print("Adi: ", ad, ", \t", "Soyadi: ", soyad , "\n",
"Ders takip puani: ",ders_takip, "\n", "Vize puan Orani: ",
      vize_orani, "\n", "Final puan Orani: ", final_orani,
      "\n","Ders takip puan orani: ", derstakip_orani, "\n",
      "Ogrenci Yil Sonu Puani 100 uzerinden toplami: ", Ogrenci_yil_sonu_notu, file=dosya)
dosya.close()