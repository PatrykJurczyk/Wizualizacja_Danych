plik = open("dane.txt","w")

for x in range(0,40,4):
    plik.write(str(x))
plik.close()
