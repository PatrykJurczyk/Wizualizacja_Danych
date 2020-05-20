class Kwadrat:
    def __init__(self, x=0):
        """Konstuktor punktu."""
        self.x = x
    def __add__(self, point):
        return Kwadrat(self.x + point.x)
    def __str__(self):
        return f'Kwadrat {self.x}'
p1 = Kwadrat(3)
p2 = Kwadrat(2)
p3 = p1 + p2
print(p3)