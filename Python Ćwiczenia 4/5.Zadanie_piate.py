# Nie rozumiem do konca reszty podpunktów. 


class Ciagi_arytmetyczne:
     atrybut1 = "piersza_wartosc"
     atrybut2 = "roznica"
     atrybut3 = "ilosc_elementow"

     def __init__(self, atrybut1, atrybut2, atrybut3):
        self.atrybut1=atrybut1
        self.atrybut2=atrybut2
        self.atrybut3=atrybut3

     def ostatni_wyraz(self):
         return self.atrybut1 + ((self.atrybut3 - 1) * self.atrybut2)
     
     def suma(self):
         return ((self.atrybut1 + objekt.ostatni_wyraz()) / 2) * self.atrybut3

     def wyswietl_dane(self):
         for x in range(self.atrybut1, objekt.ostatni_wyraz() + 1, self.atrybut2):
             print(x)



objekt = Ciagi_arytmetyczne(int(input("Podaj pierwsza wartosc: ")),int(input("roznica: ")),int(input("Podaj ilosc elementow: ")))
print("Ostatni wyraz to:", objekt.ostatni_wyraz())
print("Suma wyrazow to:", objekt.suma())
print(objekt.wyswietl_dane())