# Zad. 11 
# Napisz skrypt, który generuje tabelkę z podstawowymi wartościami funkcji trygonometrycznych. 
# Wskazówka -> wykorzystaj listy i funkcje matematyczne 

from math import *

x = ['α',   'α(0°)', 'α(30°)', 'α(45°)', 'α(60°)', 'α(90°)']
y = ['sinα', round(sin(0),2),  round(sin(pi/6),2), round(sin(pi/4),2), round(sin(pi/3),2), round(sin(pi/2),2)]
z = ['cosα', round(cos(0),2),  round(cos(pi/6),2), round(cos(pi/4),2), round(cos(pi/3),2), round(cos(pi/2),2)]
q = ['tgα',  round(tan(0),2),  round(tan(pi/6),2), round(tan(pi/4),2), round(tan(pi/3),2),'Nie istnieje']
w = ['ctgα','Nie istnieje', round(1/tan(pi/6),2), round(1/tan(pi/4),2), round(1/tan(pi/3),2), round(1/tan(pi/2),2)]
print(x)
print(y)
print(z)
print(q)
print(w)
