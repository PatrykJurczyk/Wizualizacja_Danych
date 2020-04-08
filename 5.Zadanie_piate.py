# Zad. 5 
# Napisz skrypt, który pobiera od użytkownika
# trzy liczby a, b i c. Sprawdza następujące warunki:
# czy a zawiera się w przedziale
# (0,10> oraz czy jednocześnie a>b lub b>c.
# Jeśli warunki są spełnione lub nie to ma się wyświetlić 
# odpowiedni komunikat na ekranie

a = input("Podaj pirwsza liczbe: ")
b = input("Podaj druga liczbe: ")
c = input("Podaj trzecia liczbe: ")

a = int(a)
b = int(b)
c = int(c)

if a > 0 and a <=10 and a>b and b>c:
    print("Warunki zostaly spenione :)")
else:
    print("Warunki nie zostały spełnione")
