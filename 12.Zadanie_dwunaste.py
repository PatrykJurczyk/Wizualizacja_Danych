# Zad. 12 
# Napisz skrypt, który wyświetla i oblicza tabliczkę mnożenia od 1 do 100 

for y in range(1,11):
     for x in range(1,11):
         print (str(y) ,str(" * "), str(x) ,str(" = "), x*y, end="\t")
     print() # Po co jest ten print co on robi?