class Vecteur2D:
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    
    def afficher(self):
        return "(" + str(self.x) + ", "+ str(self.y) + ")"

    def __add__(self, vecteur2D):
        return Vecteur2D(self.x + vecteur2D.x, self.y + vecteur2D.y)


vect1 = Vecteur2D()

vect2 = Vecteur2D(2,4)


print(vect1)
print(vect2)


print(vect1.afficher())



vect3 = vect1 + vect2


print(vect3.afficher())