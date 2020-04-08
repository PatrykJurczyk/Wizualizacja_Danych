import math

def ciag(a=1,r=1,ile=10):
    a1 = a + ((ile - 1) * r)
    s = ((a + a1)/2) * ile
    return(s)

print(ciag())