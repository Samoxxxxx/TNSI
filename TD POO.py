class Piece:
    # nom est une string et surface est un float
    def __init__(self,nom,surface):
    # chaque objet a pour attributs le nom de la pièce(string)
    # et la surface de celle ci(float) en m2.
    # on doit rentrer le couple nom de la pièce et la surface
    # pour chaque pièce.
        self.nom = str(nom)
        self.surface = float(surface)
    
    # Accesseurs: retournent les attributs d'un objet de cette classe
    def getNom(self):
        return self.nom
    
    def getSurface(self):
        return self.surface
    
    # Mutateur: modifient les attributs, ici la surface d'une pièce déjà
    # renseignée
    def setSurface(self,s): # s est un float
        if type(s) == float or type(s) == int:
            self.surface = s
            return True
        else:
            return False

    def setNom(self,n): # n est une string
        if type(n) == str:
            self.nom = n
            return True
        else:
            return False


class Appartement:
    # nom est une string
    def __init__(self,nom):
    #nomme l'appartement et une liste de pièces vide à remplir
        self.nom = nom
        self.pieces = []
    
    def ajouter(self,piece):
    # ajoute une pièce (instance(=objet) de la classe Piece)
        self.pieces.append(piece)
        
    def nbPieces(self):
        return len(self.pieces)
    
    def getSurfaceTotale(self):
        surfaceTot = 0.0
        for x in self.pieces:
            surfaceTot += x.surface
        return surfaceTot
    
    def getListePieces(self): # retourne la liste des pièces
        lst = []
        for i in self.pieces:
            tuple = (i.getNom(), i.getSurface())
            lst.append(tuple)
        return lst

    def getNom(self):
        return self.nom

    def setNom(self, v): # v est une string
        if type(v) == str:
            self.nom = v
            return True
        else:
            return False
    

a=Appartement('appt25')
p1=Piece("chambre", 11.1)
p2=Piece("sdbToilettes", 7)
p3=Piece("cuisine", 7)
p4=Piece("salon", 21.3)
print(p4.getNom(),p4.getSurface())
p1.setSurface(12.6)
a.ajouter(p1)
a.ajouter(p2)
a.ajouter(p3)
a.ajouter(p4)
print(a.getNom(), a.getListePieces())
print('nb pieces =', a.nbPieces(),', Surface totale =',a.getSurfaceTotale())