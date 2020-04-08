with open("dane.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")

plik = open("dane.txt","r")
print("\n")
for i in plik:
    linia = plik.read()
    print(linia)
plik.close