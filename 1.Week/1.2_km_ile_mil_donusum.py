KM = float(input("Lutfen hesaplanmasini istediginizi miktari km cinsinden giriniz: "))
MIL = KM / 1.609344
dosya=open("kmilemildonusumu.txt", "w")
print(MIL, "mil dir", file=dosya )
dosya.close()