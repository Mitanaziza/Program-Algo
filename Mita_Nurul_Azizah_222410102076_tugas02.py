x = int(input("Masukkan angka: "))

bilangan = x

if bilangan < 10:
    print ("Bilangan tersebut adalah bilangan", "genap" if (x % 2 == 0) else "gasal", "dan termasuk dalam nilai kecil")
elif bilangan >= 10 and bilangan <= 50:
    print ("Bilangan tersebut adalah bilangan", "genap" if (x % 2 == 0) else "gasal", "dan termasuk dalam nilai sedang")
if bilangan >= 50:
    print ("Bilangan tersebut adalah bilangan", "genap" if (x % 2 == 0) else "gasal", "dan termasuk dalam nilai besar")