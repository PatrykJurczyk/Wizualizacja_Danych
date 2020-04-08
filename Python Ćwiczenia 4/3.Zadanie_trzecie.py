with open("dane1.txt", "w") as plik:
    plik.write("Ala ma kota \n")
    plik.write("Kot ma Ale \n")
    plik.write("Franek Kimon \n")
    plik.write("Grzegorz \n")
    plik.write("Brzeczyszczykiewicz \n")
    
with open("dane1.txt", "r") as plik:
    for i in plik:
        print(i)