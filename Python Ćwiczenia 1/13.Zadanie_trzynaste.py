# Zad. 13 
# Stwórz słownik, gdzie zapiszesz imiona i nazwiska swoich znajomych jako klucz proszę użyć ich przezwisk (10 elementów). 
# Następnie wyświetl kilka danych odwołując się do elementów przez klucz.

kontakty = {
    "1" : "Jan Kowalski",
    2 : "Jacek Kowalski",
    3 : "Janusz Kowalski",
    4 : "Franek Kimono",
    5 : "Jan Brzeczyszczykwiecz ",
    6 : "Anna Grocka "
    
}

print(kontakty["1"][0:3])
print(kontakty[2][0:5])
print(kontakty[3][0:7])
print(kontakty[4])
print(kontakty[5][4:-1])
print(kontakty[6][5:-1])