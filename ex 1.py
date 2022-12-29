from curses.textpad import rectangle


class Rectengle:

    def __init__(self , longueur,largeur):
        self.name = "rectangle"
        self.longueur = longueur
        self.largeur = largeur
    
    def surface(self):
        return self.longueur * self.largeur 
    

    def afficher(self):
        print("{"+self.name + ", longueur:" + str(self.longueur) +"largeur:"+str(self.largeur)+ "}")


class Carre(rectangle):
    def __init__(self,longueur):
        super().__init__(longueur , longueur)
        self.name = "carre"
    


def afficher(self):
    print("{"+ self.name +",longueur: "+ str(self.longueur) + "}")


print("------------------------------")

rect = rectangle(13,15)
rect.afficher()
print(rect.surface())
print("------------------------------")

carre = Carre(16)
carre.afficher()
print(carre.surface())