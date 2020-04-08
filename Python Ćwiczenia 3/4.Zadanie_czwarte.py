import math

def monotonicznosc(y, a, b):
    if (a>0):
        return ("Funkcja jest rosnaca :)")
    elif (a<0):
        return ("Funcja jest malejaca :)")
    else:
        return ("Funkcja jest stala :)")

print(monotonicznosc(1,-1,0))