class Kwadrat:
    def __init__(self, x=0):
        """Konstuktor punktu."""
        self.x = x
    def __add__(self, point):
        return Kwadrat(self.x + point.x)
    def __str__(self):
        return f'Kwadrat {self.x}'
    def __lt__(self, point):  
        return (self.x < point.x)
    def __le__(self, point):
        return (self.x <= point.x)
    def __gt__(self, point):
        return (self.x > point.x)
    def __ge__(self, point):
        return (self.x >= point.x)



p1 = Kwadrat(2)
p2 = Kwadrat(2)
p3 = p1 + p2
p4 = p1 > p2
p5 = p1 >= p2
p6 = p1 < p2
p7 = p1 <= p2
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
