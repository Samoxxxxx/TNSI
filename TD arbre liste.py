def noeud(nom, fg = None, fd = None):
    return {'racine': nom, 'fg' : fg, 'fd': fd}


### programme principal #####
k = noeud('k')
f = noeud('f')
e = noeud('e', k, None)
b = noeud('b', e, f)
m = noeud('m')
j = noeud('j', m, None)
i = noeud('i')
d = noeud('d', i, j)
h = noeud('h')
c = noeud('c', None, h)
a = noeud('a', c, d)
A = noeud('r', a, b)
print("arbre A = ",A)


def construction_arbre(arbre):
    if arbre == None:
        return[]
	
    else:
        return [arbre['racine'],  construction_arbre(arbre['fg']), construction_arbre(arbre['fd']) ]

print("Voici la liste représentant l'arbre:", construction_arbre(A))


def representation_texte(arbre, x = 0):
    if arbre == []:
        print('*')

    else:
        print(arbre[0])
        x = x+1
        print('-' * x, end ='')
        representation_texte(arbre[1], x)
        print('-' * x, end ='')
        representation_texte(arbre[2], x)

print("Voici la représentation texte de l'arbre:")
representation_texte(construction_arbre(A))

def hauteur_arbre(arbre):
    if arbre == []:
        return -1 # Retourne -1 et non 0 car il n'y a pas de racine vu qu'il n'y a pas d'arbre
    
    else:
        h1 = 1 + hauteur_arbre(arbre[1])
        h2 = 1 + hauteur_arbre(arbre[2])
        return max(h1, h2)

print("Voici la hauteur de l'arbre:", hauteur_arbre(construction_arbre(A)))

def parcours_prefixe(arbre):
    if arbre != []:
        print(arbre[0], end = ',')
        parcours_prefixe(arbre[1])
        parcours_prefixe(arbre[2])

print("Voici le parcours préfixe de l'arbre:")
parcours_prefixe(construction_arbre(A))
print("\n")

def parcours_postfixe(arbre):
    if arbre != []:
        parcours_postfixe(arbre[1])
        parcours_postfixe(arbre[2])
        print(arbre[0], end = ',')

print("Voici le parcours postfixe de l'abre:")
parcours_postfixe(construction_arbre(A))
print("\n")

def parcours_infixe(arbre):
    if arbre != []:
        parcours_infixe(arbre[1])
        print(arbre[0], end = ',')
        parcours_infixe(arbre[2])

print("Voici le parcours infixe de l'arbre:")
parcours_infixe(construction_arbre(A))