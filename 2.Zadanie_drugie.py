# Zad. 2 
# Napisz skrypt, który pobiera od użytkownika dwie wartości i mnoży je przez siebie.
# Wynik wyświetla na ekranie (użyj instrukcji readline() i write()).

#Zapytać się jak zrobić mnożenie. 

x = input("Podaj liczbe: ")
y = input("Podaj liczbe: ")
e = int(x)
i = int(y)
z = e * i
g = str(z)
print(z)
f = open("plik.txt","a+")
f.write(x) + f.write(" * ")
f.write(y) + f.write(" = ")
f.write(g)
f.close()




f = open("plik.txt","r")
print(f.readline())
f.close()


