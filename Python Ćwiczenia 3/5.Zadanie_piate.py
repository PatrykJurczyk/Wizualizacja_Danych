import math

def spr(a1,a2):
    if (a1 == a2):
        return ("Proste sa rownolegle :)")
    elif (a1*a2 == (-1)):
        return ("Proste sa prostopadle :)")
    else:
        return ("Proste nie sa ani prostopadle ani rownolegle :(")

print(spr(1,3))
