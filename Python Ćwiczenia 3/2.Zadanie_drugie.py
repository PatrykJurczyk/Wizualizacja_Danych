# Zad. 2 
# Wygeneruj losowo macierz 4x4 i wykorzystując 
# Python Comprehension  zdefiniuj listę, 
# która będzie zawierała tylko elementy znajdujące 
# się na przekątnej. 
import random

x = random.randint(0, 16)
print(x)
A = [1, 2, 3, 1,
     4, 5, 6, 2,
     7, 8, 9, 4,
     4, 6, 6, 7]

print(A)
print(A[0])
B = [x for x in A]
print(B)