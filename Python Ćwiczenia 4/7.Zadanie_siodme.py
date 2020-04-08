class Robaczek:

    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
   
    def gora(self,ile_krokow):
        self.ile_krokow = ile_krokow
        self.x = self.x + (self.krok * self.ile_krokow)
        return self.x
    
    def dol(self,ile_krokow):
        self.ile_krokow = ile_krokow
        self.x = self.x - (self.krok * self.ile_krokow)
        return self.x
    
    def prawo(self,ile_krokow):
        self.ile_krokow = ile_krokow
        self.y = self.y + (self.krok * self.ile_krokow)
        return self.y
    
    def lewo(self,ile_krokow):
        self.ile_krokow = ile_krokow
        self.y = self.y - (self.krok * self.ile_krokow)
        return self.y
    
    def aktuana_pozycja(self):
        return self.x

    def aktuana_pozycja1(self):
        return self.y


objekt = Robaczek(int(input("Podaj poczatkowa pozycje gora-dol: ")),int(input("Podaj poczatkowa pozycje prawo-lewo: ")),int(input("Podaj krok: ")))
print("Pozycja teraz: ", objekt.gora(int(input("Podaj o ile krokow w gore przesunac: "))))
print("Pozycja teraz: ", objekt.dol(int(input("Podaj o ile krokow w dol przesunac: "))))
print("Pozycja teraz: ", objekt.prawo(int(input("Podaj o ile krokow w prawo przesunac: "))))
print("Pozycja teraz: ", objekt.lewo(int(input("Podaj o ile krokow w lewo przesunac: "))))
print("Aktualna pozycja x: ", objekt.aktuana_pozycja())
print("Aktualna pozycja y: ", objekt.aktuana_pozycja1())