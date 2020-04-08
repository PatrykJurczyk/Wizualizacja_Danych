x = {
    "Chleb" : "sztuka",
    "Maslo" : "sztuka",
    "Kiebasa" : "waga",
    "ser" : "waga"
}
print(type(x))
print(x["Chleb"])
lista = [k for k , y in x.items() if y == "sztuka"]
print(lista)