#Aplikasi game secret number

secret_number = 777

guess_number=int (input("Masukkan Tebak Angka:"))

while guess_number !=secret_number:
    print("Tebakan salah, Silahkan coba lagi")
    guess_number:int(input("Masukkan Tebak Angka:"))

print("Selamat.. !!, Tebakan anda benar!!")
print("kode ini saya buat di codespace")