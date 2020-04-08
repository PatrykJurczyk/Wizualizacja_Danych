class Slowa:
    atrybut1 = str(input("Podaj pierwsze slowo: "))
    atrybut2 = str(input("Podaj drugie slowo: "))

    def palindrom(self):
        if (self.atrybut2 == self.atrybut1[::-1]):
            return True
        return False

    
    def anagramy(self):
        a = sorted(self.atrybut1)
        b = sorted(self.atrybut2)
        if(a == b):
            return True
        return False


    def wyrazy(self):
        print(self.atrybut1)
        print(self.atrybut2)


objekt = Slowa()
print("Palindrom", objekt.palindrom())
#print("Metagramy", objekt.metagramy()) <---- Nie mam pomysłu 
print("Anagramy", objekt.anagramy())