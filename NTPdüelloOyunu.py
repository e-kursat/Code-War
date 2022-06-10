import time
import random

class Player:
    # class attributes
    health = 100
    
    # yapıcı attributes
    def __init__(self, no, name, surname, age, team):
        self.no = no
        self.name = name    # genelde aynı değişken kullanılır.
        self.soyisim = surname  # farklı değişkenler de kullanılabilir.
        self.yas = age
        self.takım = team
        
class Weapon:
    def __init__(self, no, name, damage, ammo, reloadtime):
        self.no = no
        self.name = name
        self.damage = damage
        self.ammo = ammo
        self.mermidegistirmehizi = reloadtime
        
    def silahBilgi(self):
        print(f"İsim: {self.name}, Hasarı: {self.damage}, Mermi Miktarı: {self.ammo}, Yenileme Süresi: {self.mermidegistirmehizi}")

oyuncu1 = Player(1, "Kürşat Emre", "Özkara", 20, "B")
oyuncu2 = Player(2, "Alp Doruk", "Şengün", 18, "A")

silah1 = Weapon(1, "RPG", 50, 2, 5)
silah2 = Weapon(2, "M4A1", 10, 6, 1)

while(oyuncu1.health > 0 and oyuncu2.health > 0):
    turn = random.randint(1, 2)
    
    if turn == oyuncu1.no:
        silah_sec = random.randint(1, 2)
        
        if silah_sec == silah1.no:
            oyuncu2.health -= silah1.damage            
            for i in "BOOM!!!!!!!!!!!":
                print(f"\a{i}")
            print(f"\a{oyuncu2.name} kafasına {silah1.name} yedi!")
            print(f"{oyuncu2.name} adlı oyuncunun kalan canı: {oyuncu2.health}\n")
            time.sleep(3)
            
        elif silah_sec == silah2.no:
            oyuncu2.health -= silah2.damage
            print(f"{oyuncu2.name} kafasına {silah2.name} yedi!")
            print("Birisi leblebi mi fırlattı??")
            print(f"{oyuncu2.name} adlı oyuncunun kalan canı: {oyuncu2.health}\n")
            time.sleep(3)

    else:
        silah_sec = random.randint(1, 2)
        
        if silah_sec == silah1.no:
            oyuncu1.health -= silah1.damage
            for i in "BOOM!!!!!!!!!!!":
                print(f"\a{i}")
            print(f"\a{oyuncu1.name} kafasına {silah1.name} yedi!")
            print(f"{oyuncu1.name} adlı oyuncunun kalan canı: {oyuncu1.health}\n")
            time.sleep(3)
            
        elif silah_sec == silah2.no:
            oyuncu1.health -= silah2.damage
            print(f"{oyuncu1.name} kafasına {silah2.name} yedi!")
            print("Birisi leblebi mi fırlattı??")
            print(f"{oyuncu1.name} adlı oyuncunun kalan canı: {oyuncu1.health}\n")
            time.sleep(3)

            
if oyuncu1.health <= 0:
    print(f"{oyuncu1.name} adlı oyuncunun helvası yenecek.")
    print("Esselaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa..")
    
elif oyuncu2.health <= 0:
    print(f"{oyuncu2.name} iyi insandı.")
    print(f"{oyuncu2.name} adlı oyuncudan hiç beklenmezdi")