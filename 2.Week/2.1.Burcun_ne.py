# Koc burcu (21 Mart- 20 Nisan)
# Boga burcu (21 Nisan- 21 Mayis)
# Ikizler burcu (22 Mayis- 22 Haziran)
# Yengec burcu (23 Haziran- 22 Temmuz)
# Aslan burcu (23 Temmuz- 22 Agustos)
# Basak burcu (23 Agustos- 22 Eylul)
# Terazi burcu (23 Eylul- 22 Ekim)
# Akrep burcu (23 Ekim- 21 Kasim)
# Yay burcu (22 Kasim- 21 Aralik)
# Oglak burcu (22 Aralik- 21 Ocak)
# Kova burcu (22 Ocak- 19 Subat)
# Balik burcu (20 Subat- 20 Mart)

burc_ayi = input("Lutfen Dogdugunuz Ayi Giriniz: ")
burc_gunu = input("Lutfen Dogdugunuz Gunu Giriniz: ")

# ocak = mart = mayis = temmuz = agustos = ekim = aralik = 31
# nisan = haziran = eylul = kasim = 30
# subat = 28


if (bool(burc_ayi) == True) and (bool(burc_gunu) == True):
    burc_gunu = int(burc_gunu)
    if burc_ayi == "ocak":
        print("Dogum gununuz", burc_gunu, "Ocak")
        if 1 <= burc_gunu <= 21:
            print("Burcunuz 'Oglak' tir.")
        elif 22 <= burc_gunu <= 31:
            print("Burcunuz 'Kova' dir.")
        else:
            print("Lutfen girmis oldugunuz sayiyi 1 ile 31 arasinda secerek tekrar deneyiniz...")
    elif burc_ayi == "subat":
        print("Dogum gununuz", burc_gunu, "Subat")
        if 1 <= burc_gunu <= 19:
            print("Burcunuz 'Kova' dir.")
        elif 20 <= burc_gunu <= 28:
            print("Burcunuz 'Balik' tir.")
        elif burc_gunu == 29:
            print("Bu tarih 4 yilda bir gerceklesir 'SANSLISINIZ' ama malesef burcunuz 'Balik' tir. Hahaha :D")
        else:
            print("Lutfen girmis oldugunuz sayiyi 1 ile 29 arasinda secerek tekrar deneyiniz...")

    elif burc_ayi == "mart":
        print("Dogum gununuz", burc_gunu, "Mart")
        if 1 <= burc_gunu <= 20:
            print("Burcunuz 'Balik' tir.")
        elif 21 <= burc_gunu <= 31:
            print("Burcunuz 'Koc' tur.")
        else:
            print("Lutfen girmis oldugunuz sayiyi 1 ile 31 arasinda secerek tekrar deneyiniz...")
    elif burc_ayi == "nisan":
        print("Dogum gununuz", burc_gunu, "Nisan")
        if 1 <= burc_gunu <= 20:
            print("Burcunuz 'Koc' tur.")
        elif 21 <= burc_gunu <= 30:
            print("Burcunuz 'Boga' dir.")
        else:
            print("Lutfen girmis oldugunuz sayiyi 1 ile 30 arasinda secerek tekrar deneyiniz...")
    elif burc_ayi == "mayis":
        print("Dogum gununuz", burc_gunu, "Mayis")
        if 1 <= burc_gunu <= 21:
            print("Burcunuz 'Boga' dir.")
        elif 22 <= burc_gunu <= 31:
            print("Burcunuz 'Ikizler' dir.")
        else:
            print("Lutfen girmis oldugunuz sayiyi 1 ile 31 arasinda secerek tekrar deneyiniz...")
    elif burc_ayi == "haziran":
        print("Dogum gununuz", burc_gunu, "Haziran")
        if 1 <= burc_gunu <= 22:
            print("Burcunuz 'Ikizler' dir.")
        elif 23 <= burc_gunu <= 30:
            print("Burcunuz 'Yengec' tir.")
        else:
            print("Lutfen girmis oldugunuz sayiyi 1 ile 30 arasinda secerek tekrar deneyiniz...")
    elif burc_ayi == "temmuz":
        print("Dogum gununuz", burc_gunu, "Temmuz")
        if 1 <= burc_gunu <= 22:
            print("Burcunuz 'Yengec' tir.")
        elif 23 <= burc_gunu <= 31:
            print("Burcunuz 'Aslan' dir.")
        else:
            print("Lutfen girmis oldugunuz sayiyi 1 ile 31 arasinda secerek tekrar deneyiniz...")
    elif burc_ayi == "agustos":
        print("Dogum gununuz", burc_gunu, "Agustos")
        if 1 <= burc_gunu <= 22:
            print("Burcunuz 'Aslan' dir.")
        elif 23 <= burc_gunu <= 31:
            print("Burcunuz 'Basak' tir.")
        else:
            print("Lutfen girmis oldugunuz sayiyi 1 ile 31 arasinda secerek tekrar deneyiniz...")
    elif burc_ayi == "eylul":
        print("Dogum gununuz", burc_gunu, "Eylul")
        if 1 <= burc_gunu <= 22:
            print("Burcunuz 'Basak' tir.")
        elif 23 <= burc_gunu <= 30:
            print("Burcunuz 'Terazi' dir.")
        else:
            print("Lutfen girmis oldugunuz sayiyi 1 ile 30 arasinda secerek tekrar deneyiniz...")
    elif burc_ayi == "ekim":
        print("Dogum gununuz", burc_gunu, "Ekim")
        if 1 <= burc_gunu <= 22:
            print("Burcunuz 'Terazi' dir.")
        elif 23 <= burc_gunu <= 31:
            print("Burcunuz 'Akrep' tir.")
        else:
            print("Lutfen girmis oldugunuz sayiyi 1 ile 31 arasinda secerek tekrar deneyiniz...")
    elif burc_ayi == "kasim":
        print("Dogum gununuz", burc_gunu, "Kasim")
        if 1 <= burc_gunu <= 21:
            print("Burcunuz 'Akrep' tir.")
        elif 22 <= burc_gunu <= 30:
            print("Burcunuz 'Yay' dir.")
        else:
            print("Lutfen girmis oldugunuz sayiyi 1 ile 30 arasinda secerek tekrar deneyiniz...")
    elif burc_ayi == "aralik":
        print("Dogum gununuz", burc_gunu, "Aralik")
        if 1 <= burc_gunu <= 21:
            print("Burcunuz 'Yay' dir.")
        elif 22 <= burc_gunu <= 31:
            print("Burcunuz 'Oglak' tir.")
        else:
            print("Lutfen girmis oldugunuz sayiyi 1 ile 31 arasinda secerek tekrar deneyiniz...")
    else:
        print(
            "Lutfen girmis oldugunuz AY ve GUN kismini dogru yazdiginizdan emin olarak \n ve Turkce karakterler kullanmadan kucuk harflerle bir daha deneyiniz...")

else:
    print("Lutfen Bos gecmeyin...")
