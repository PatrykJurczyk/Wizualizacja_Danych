# Zad. 14 
# Stwórz słownik skrótów powszechnie używanych w smsach. 
# Jako klucz niech będzie skrót a jako wartość zdanie. 
# Skopiuj słownik do innego słownika

x1 = {
    "zw" : "Zaraz wracam ",
    "bd" : "Bedzie",
    "Gn" : "GoodNight",
    "Tbh": "To be Honest"

}

x2 = {

}

print(x1['zw'])
print(x1['bd'])
print(x1['Gn'])
print(x1['Tbh'])

print("\n")

x2 = x1.copy()
print(x2)

