# Nama  : Mita Nurul Azizah
# NIM   : 222410102076

print(30*"=" + " CHECK SELISIH HURUF " + 30*"=" + "\r\n")
input_data = int(input("Berapa huruf yang ingin anda inputkan? : "))
userku = 0
listempty  = []

while userku < input_data :
    userku += 1
    words = input(f"Masukkan kata ke {userku} : ")
    listempty.append(words)
for huruf in listempty :
    print("Hasil : ")
    for x in range(len(huruf)):
        if x == len(huruf)-1:
            break
        kata_saya = huruf[x]
        convert = ord(kata_saya) 
        hasil = abs(convert - (ord(huruf[x + 1])))
        if convert < ord(huruf[x + 1]):
            print(f"{kata_saya} kurang dari {huruf[x + 1]}, selisih ialah {hasil}")
        else :
            print(f"{kata_saya} lebih dari {huruf[x + 1]}, selisih ialah {hasil}")