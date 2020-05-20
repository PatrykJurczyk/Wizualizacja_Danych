class Material:
    

    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        return self.rodzaj

class Ubrania(Material):

    def __init__(self,rozmiar,kolor,dla_kogo,rodzaj,dlugosc,szerokosc):
        super().__init__(rodzaj,dlugosc,szerokosc)
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo
    

    def wyswietl_dane(self):
        return self.rozmiar , self.kolor , self.dla_kogo

class Sweter(Ubrania):

    def __init__(self,rodzaj_swetra,rozmiar,kolor,dla_kogo,rodzaj,dlugosc,szerokosc):
        super().__init__(rozmiar,kolor,dla_kogo,rodzaj,dlugosc,szerokosc)
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_dane1(self):
        return self.rodzaj_swetra

o = Ubrania(32,"cza","das","dasd",313,432)

