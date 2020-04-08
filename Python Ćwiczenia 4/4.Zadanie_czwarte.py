# Zad. 4
# Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:
# nazwa_produktu, ilosc, jednostka_miary, cena_jed oraz metody:
# konstruktor – który nadaje wartości
# wyświetl_produkt() – drukuje informacje o produkcie na ekranie

# ile_produktu() – informacje ile danego produktu ma 
# być czyli ilosc + jednostka_miary np. 1 szt., 3 kg itd.

# ile_kosztuje() – oblicza ile kosztuje dana ilość produktu 
# np. 3 kg ziemniaków a cena_jed wynosi 2 zł/kg 
# wówczas funkcja powinna zwrócić wartość 3*2

class NaZakupy:
     atrybut1 = "nazwa_produktu: "
     atrybut2 = "ilosc: "
     atrybut3 = "jednostka_miary: "
     atrybut4 = "cena_jed: "



     def __init__(self, atrybut1, atrybut2, atrybut4, atrybut3):
        self.atrybut1=atrybut1
        self.atrybut2=atrybut2
        self.atrybut4=atrybut4
        self.atrybut3=atrybut3
         
     def nazwa_produktu(self):
         return self.atrybut1
    
     def ile_produktu(self):
        return str(self.atrybut2) + self.atrybut3

     def ile_kosztuje(self):
        return self.atrybut2 * self.atrybut4

obiekt = NaZakupy(str(input("Podaj nazwe produktu: ")),int(input("ilosc: ")),int(input("cena jednostki: ")),str(input("jednostka miary: ")))
print("Nazwa produktu", obiekt.nazwa_produktu())
print("cena za całosc:",obiekt.ile_kosztuje())
print("Ilosc",obiekt.ile_produktu())