def p_valeur(pile):
    
    """
    - prend en paramètre une pile pile
    - renvoie le sommet de la pile
    Exemple :
    >>> p_valeur([2, 3, 5])
    >>> 5
    >>> p_valeur([])
    >>> None
    """
    
    if len(pile) != 0:
        l_pile = len(pile)
        return pile[l_pile-1]
    else:
        return None

   
assert p_valeur([]) is None
assert p_valeur([2, 3, 5]) == 5


def p_depile(pile):
    
    """
    - prend en paramètre une pile pile
    - dépile le dernier élément saisi
    Exemple :
    >>> p_valeur([2, 3, 5])
    >>> 5
    >>> p_valeur([])
    >>> None
    """

    if len(pile) != 0:
        v_depile = pile.pop(len(pile)-1)
        return v_depile
    else:
        return None
    

p=[2, 3, 5]
assert p_depile(p) == 5
assert p == [2, 3]
assert p_depile([]) is None


def p_empile(pile, v):
    
    """
    - prend en paramètre une pile et une valeur v
    - empile la valeur v
    Exemple :
    >>> pile = [2, 3]
    >>> p_empile(pile, 5)
    >>> pile
    >>> [2, 3, 5]
    """
    pile.append(v)
    return pile
 

pile = [2, 3]
p_empile(pile, 5)
assert pile == [2, 3, 5]


def f_valeur(file):
    
    """
    - prend en paramètre une file
    - renvoie la valeur à l’avant de la file ou None si la file est vide
    Exemple :
    >>> f_valeur([2, 3, 5])
    >>> 5
    >>> f_valeur([])
    >>> None
    """
    
    if len(file) != 0:
        l_file = len(file)
        return pile[l_file -1]
    else:
        return None


assert f_valeur([]) is None
assert f_valeur([2, 3, 5]) == 5


def f_defile(file):
    
    """
    - prend en paramètre une file
    - défile l'élément situé à l'avant de la file
    - renvoie la valeur défilée ou None si la file est vide
    Exemple :
    >>> file = [2, 3, 5, 8]
    >>> f_defile(file)
    >>> 8
    >>> file
    >>> [2, 3, 5]
    """
    
    if len(file) != 0:
        v_defile = file.pop(len(file)-1)
        return v_defile
    else:
        return None


file = [2, 3, 5, 8]
assert f_defile(file) == 8
assert file == [2, 3, 5]


def f_enfile(file, v):

    """
    - prend en paramètre une file et une valeur v
    - enfile la valeur v à l'arrière de la file
    Exemple :
    >>> file = [2, 3, 5, 8]
    >>> f_enfile(file, 1)
    >>> file
    >>> [1, 2, 3, 5, 8]
    """

    file.insert(0, v)
    return file


file = [2, 3, 5, 8]
f_enfile(file, 1)
assert file == [1, 2, 3, 5, 8]


def echange_FondSommet(p):

    """ Échange le sommet et le fond de la pile p (p[-1] <-> p[0]) """

    index_fond = 0
    index_sommet = len(p)-1
    element_fond = p.pop(index_fond)
    element_sommet = p.pop(index_sommet-1)
    p.insert(index_fond, element_sommet)
    p.insert(index_sommet, element_fond)
    return p

def pile_copie(p):

    """Fonction pile_copie(p) recevant une pile p en paramètre et renvoyant une copie p2 de p."""

    p2 = p.copy()
    return p2


def pile_inversee(p):

    """Fonction pile_inversee(p) recevant une pile p en paramètre et renvoyant la pile p inversée."""

    p.reverse()
    return p


### programme principal #####

print(p_valeur([]))
print(p_valeur([2, 3, 5]) == 5)
p=[2, 3, 5]
print("contenu de la pile : ",p)
print("depiler un element = ",p_depile(p))
print("contenu de la pile : ",p)
print("empiler un element = ",p_empile(p,128))
print("contenu de la pile : ",p)
print("echanger le sommet avec le fond = ",echange_FondSommet(p))
print("contenu de la pile : ",p)
print("copie de pile, pile résultante = ",pile_copie(p))
print("pile inversée, pile résultante = ",pile_inversee(p))
print("contenu de la pile d'origine' : ",p)