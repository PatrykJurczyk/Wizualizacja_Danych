# Zad. 10 
# Napisz skrypt, który rysuje wieżę z literek. 
# Użytkownik podaje wysokość wieży ale nie więcej jak 10

a = input("Podaj wysokość wieży: ")
b = int(a)

for i in range(2):
    if b > 10:
        print("Podałeś za dużą liczbę :)")
    else:
        for j in range(1,b+1):
            print(j * "A")

