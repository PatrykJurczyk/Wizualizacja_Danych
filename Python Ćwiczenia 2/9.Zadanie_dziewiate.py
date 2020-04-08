# Zad. 9 
# Napisz skrypt, który odczytuje od użytkownika 
# liczbę wielocyfrową i sumuje jej cyfry. 
# Wynik wyświetla na ekranie. 
# Wykorzystaj pętle while.

#Petla While poprosic o wytłumaczenie.


a = input("Podaj liczbe wielocyfrowa: ")
print(a)
i = 0
wynik = int(a[0])
print(a[0])
while i < len(a):
    i+=1
    x = a[i]
    print(x)
    wynik += int(x)
    break
print(wynik)

# liczba = input("Podaj liczbe wielocyfrowa: ")
# print (liczba)
# wynik = 0
# wynik = sum([int(cyfra) for cyfra in(str(liczba))])
# print(wynik)
