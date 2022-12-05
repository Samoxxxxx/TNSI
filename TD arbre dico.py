A = { 'r' : ['a','b'], 'a' : ['c','d'], 'b' : ['e','f'],
	'c' : ['','h'], 'd' : ['i', 'j'], 'e' : ['k',''], 'f' : ['',''],
     'h' : ['',''], 'i': ['',''], 'j' : ['m',''], 'k' : ['',''], 'm' : ['','']}


def hauteur_arbre(arbre, noeud='r'):
    if arbre[noeud][0] == '' and arbre[noeud][1] == '':
        return 0

    elif arbre[noeud][0] == '':
        return 1 + hauteur_arbre(arbre, arbre[noeud][1])

    elif arbre[noeud][1] == '':
        return 1 + hauteur_arbre(arbre, arbre[noeud][0])

    else:
        return 1 + max(hauteur_arbre(arbre, arbre[noeud][0]), hauteur_arbre(arbre, arbre[noeud][1]))

print("Voici la hauteur de l'arbre:", hauteur_arbre(A))

def parcours_prefixe(arbre, noeud='r'):
    if noeud != '':
        print(noeud, end = ',')
        parcours_prefixe(arbre, arbre[noeud][0])
        parcours_prefixe(arbre, arbre[noeud][1])

print("Voici le parcours prefixe de l'arbre:")
parcours_prefixe(A)
print("\n")

def parcours_postfixe(arbre, noeud='r'):
    if noeud != '':
        parcours_postfixe(arbre, arbre[noeud][0])
        parcours_postfixe(arbre, arbre[noeud][1])
        print(noeud, end = ',')

print("Voici le parcours postfixe de l'arbre:")
parcours_postfixe(A)
print("\n")

def parcours_infixe(arbre, noeud='r'):
    if noeud != '':
        parcours_infixe(arbre, arbre[noeud][0])
        print(noeud, end = ',')
        parcours_infixe(arbre, arbre[noeud][1])

print("Voici le parcours infixe de l'arbre:")
parcours_infixe(A)