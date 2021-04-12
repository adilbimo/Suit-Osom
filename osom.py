# Import Module 
import os 
import re 
import time
import random 

#Clear Terminal
os.system("cls" if os.name == "nt" else "clear")  

while True:

    print("\nGunting - Batu - Kertas!!\n") 

    kamu = input("Pilih => [G]unting, [B]atu, [K]ertas > ") 

    if not re.match("[GgBbKk]", kamu):
        print("Pilih (G, B, Atau K)")
        print("[G]unting, [B]atu, [K]ertas")
        continue 

    print("===============================")

    print("kamu : " + kamu)
    
    pilihan = ["G", "B", "K"]

    lawan = random.choice(pilihan) 
    print("Lawan : " + lawan)

    # print("<==>")

    if lawan  == str.upper(kamu):
        print("Serii :b")
    # Gunting
    elif lawan == pilihan[0] and kamu == "B":
        print("Kamu Menang :)")
    elif lawan == pilihan[0] and kamu == "K":
        print("Kamu Kalah :(")

    # Batu
    elif lawan == pilihan[1] and kamu == "G":
        print("Kamu Kalah :)")
    elif lawan == pilihan[1] and kamu == "K":
        print("Kamu Menang :(")

    # Kertas
    elif lawan == pilihan[2] and kamu == "G":
        print("Kamu Kalah :(")
    elif lawan == pilihan[2] and kamu == "B":
        print("Kamu Menang :)")
    
    else:
        print("Kamu Menang :v")

    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")  

    


    


        









