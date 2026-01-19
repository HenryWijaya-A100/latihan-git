#Game Tebak Angka

secret = 234
attempts = 0

print("🎮 GAME TEBAK ANGKA 🎮")
print("=" * 40)

while True:
    try:
        guess = int(input("Masukkan tebak angka: "))
        attempts += 1
        
        if guess == secret:
            print(f"🎉 SELAMAT! Anda benar! 😊")
            print(f"Angka rahasia: {secret}")
            print(f"Jumlah percobaan: {attempts}")
            break
        elif guess < secret:
            print("📈 Angka terlalu kecil!")
        else:
            print("📉 Angka terlalu besar!")
    except ValueError:
        print("❌ Masukkan angka yang valid!")
        
print("\nTerima kasih telah bermain! 👋")