# Zad. 11 
# Napisz skrypt, który rysuje diament.
# Użytkownik podaje wysokość nie mniej jak 3 i nie więcej jak 9 wysokość=3 

a = input("Podaj wysokość diamentu: ")
b = int(a)

for i in range(1):
    if b < 3:
        print("Za mało podaj wiecej jak 3!!")
    elif b > 9:
        print("Za dużo podaj mniej jak 9!!!")
    else:
        for j in range(1,b+1):
            print(j * "A")