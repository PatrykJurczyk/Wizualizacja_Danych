# Zad 1
#Zdefiniuj następujące zbiory, wykorzystując Python comprehension: 
#A={1/x:  x<1,10>} 
#B={1, 2, 4, 8,…, 210} 
#C={x: xB i x jest liczbą podzielną przez 4} 

A = [1/x for x in range(1,11)]
print(A)
B = [x*2 for x in range(1,211)]
print(B)
C = [x for x in B if x % 4 == 0]
print(C)