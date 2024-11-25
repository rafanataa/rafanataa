import random
import os
class ceritaku:
    def _init_(self):
        Makanan = [ "Ayam crispy", "Nuggets"]
        randomMakanan = random.choice(Makanan)

        Restaurant = ["KFC", "Mc Donald"]
        randomRestaurant = random.choice(Restaurant)

        Makanan2 = ["Saus tomat", "Saus sambal"]
        randomMakanan2 = random.choice(Makanan2)
        Minuman = ["Sprite", "Cocacola", "Fanta"]
        randomMinuman = random.choice(Minuman)
        os.system("cls")
        print(f"Saya makan nasi,saya memesan paket combo dan menyajikan makanan di atas meja,saya makan nasi dengan makanan {randomMakanan} pakai {randomMakanan2} dan saya mendapatkan minuman {randomMinuman},saya makan di{randomRestaurant}")
        def main():
            run = ceritaku()

            if _name_ == "_main_":
                main()
