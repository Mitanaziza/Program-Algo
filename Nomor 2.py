# Nama  : Mita Nurul Azizah
# NIM   : 222410102076

print(f"""Daftar kode sapi :
      1.    Sapi Warrior    : 690 hari
      2.    Sapi Mage       : 420 hari
      3.    Sapi Assassin   : 530 hari
      4.    Sapi Nolep      : 330 hari
      """)
Sapi_Warrior    = 690
Sapi_Mage       = 420
Sapi_Assassin   = 530
Sapi_Nolep      = 330
inputdata = int(input("Masukkan jumlah sapi : "))
batas = 0
totalakhir = 0
while batas < inputdata :
    inputdata = int(input("Masukkan kode sapi : "))
    if inputdata == 1 :
        totalakhir += Sapi_Warrior
    elif inputdata == 2 :
        totalakhir += Sapi_Mage
    elif inputdata == 3 :
        totalakhir += Sapi_Assassin
    elif inputdata == 4 :
        totalakhir += Sapi_Nolep
    else :
        print(f"Code Sapi {inputdata} Tidak Ada")
    batas += 1
totaltahun = totalakhir // 365
totalbulan = totalakhir % 365 // 30
totalhari = totalakhir % 365 % 30
print(f"Jumlah hari yang diperlukan ialah : {totaltahun} Tahun, {totalbulan} Bulan, dan {totalhari} Hari")