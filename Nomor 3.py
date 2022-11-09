# Nama  : Mita Nurul Azizah
# NIM   : 222410102076

Data = input("Masukkan kata : ")
condition = False
kiri = ['q','w','e','r','t','a','s','d','f','g','z','x','c','v','b']
kanan = ['y','u','i','o','p','h','j','k','l','n','m']

for a in range(len(Data) - 1):
    if Data[a] in kanan and Data[a + 1] in kanan:
        penjelasan = f"Penjelasan: Karakter yang berdempetan yakni {Data[a]} dan {Data[a + 1]} berada di satu tangan (kanan)"
        break
    elif Data[a] in kiri and Data[a + 1] in kiri :
        penjelasan = f"Penjelasan: Karakter yang berdempetan yakni {Data[a]} dan {Data[a + 1]} berada di satu tangan (kiri)"
        break
    else :
        condition = True
        penjelasan = "Penjelasan: Setiap karakter selalu bergantian tangan."

print(condition, penjelasan, sep="\r\n")