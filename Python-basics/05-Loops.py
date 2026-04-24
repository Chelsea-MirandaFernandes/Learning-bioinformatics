#HelloWorld - 24 avril 2027


# Boucle for : parcourt chaque élément d'une séquence (liste, chaîne, etc...) et exécute un bloc de code pour chacun. 
genes = ["BRCA1", "BRCA2", "TP53"]
for gene in genes:
    print("Analyse du gène :", gene)



# Range () : pour répéter N fois. 
## Range (n) : génère les nombres de 0 à n-1
for i in range (5):
    print(i) # 0 1 2 3 4

## Range (début, fin) 
for i in range (1, 6):
    print(i) # 1 2 3 4 5 

## Range (début, fin, pas)
for i in range (0, 10, 2):
    print(i) # 0 2 4 6 8

## Affiche l'index ET la valeur avec enumerate (séquence) : génère des paires (index, valeur) pour chaque élément de la séquence.
genes = ["BRCA1", "EGFR", "TP53"]
for i, gene in enumerate (genes) : # i = index, gene = valeur
    print(f"Index {i} : {gene}") 



# Boucle while : while répète un bloc tant qu'une condition est vraie (toujours prévoir une sortie pour les boucles infinies)
compteur = 0 
while compteur < 5 :
    print("Compteur :", compteur)
    compteur += 1 # Permet de ne pas faire une boucle infinie.



# Break et continue :
## Break : sortir immédiatement de la boucle 
for i in range (10):
    if i == 5 : 
        break 
    print(i)

## Continue : passer à l'itération suivante
for i in range (10):
    if i % 2 == 0 : # si i est pair 
        continue # on saute cette itération
    print(i) # 1 3 5 7 9 



# List comprehension : syntaxe concise pour créer une liste à partir d'une autre. 
## Version longue 
carres = [] 
for x in range (5):
    carres.append (x ** 2)
print(carres)

## Version list comprehension - équivalent, plus concis 
carres = [x ** 2 for x in range (5)] # [EXPRESSION for VARIABLE in SEQUENCE]
print(carres) 

## Avec condition (filtrer): seulement les pairs 
pairs = [x ** 2 for x in range (10) if x % 2 == 0] # [EXPRESSION for VARIABLE in SEQUENCE if CONDITION]
print(pairs) 

## Application bio : longueur de chaque gène
genes = ["BRCA1", "TP53", "EGFR", "MYC"]
longueurs = [len (g) for g in genes] # len (g) compte le nombre de lettres/caractères. Exemple : B-R-C-A-1 = 5.
print(longueurs)



# Opérateurs : 
x += 5 # x = x + 5 (ajouter 5)
x -= 3 # x = x - 3 (soustraire 3)
x *= 2 # x = x * 2 (multiplier par 2)
x /= 4 # x = x / 4 (diviser par 4)



# Exercice 1 : Boucle for sur une liste de 5 notes — affiche chaque note et si elle est >= 10
notes = [12, 18, 7, 4, 20]
for note in notes: # Boucle sur les notes de la liste
    if note >= 10: # Teste chaque note individuellement
        print(note) # Affiche la note si elle est >= 10



# Exercice 2 :  Utiliser range() pour afficher les nombres de 1 à 20 uniquement pairs
for i in range (2, 21,2):
    print (i)



# Exercice 3 : Boucle while qui compte de 100 à 0 par pas de 10
## Option 1 :
compteur = 100
while compteur != 0 :
    compteur = compteur - 10 
    print (compteur)

## Option 2 :
compteur = 100
while compteur > 0 :
    compteur -= 10 # Équivalent à compteur = compteur - 10. On soustrait 10 à compteur et on stocke le résultat. 
    print (compteur)

## Option 3 avec for :
for i in range (100, -1, -10) : # Va de 100 à 0 par de -10
    print (i)



# Exercice 4 : Utiliser break pour arrêter une boucle quand on trouves le mot 'TP53' dans une liste
genes = ["BRCA1", "BRCA2", "EGFR", "TP53", "MYC"]
for gene in genes : # Boucle sur chaque élément
    if gene == "TP53" : # Vérifie si l'élément courant est "TP53"
        print(f"Trouvé : {gene}")
        break # Sort de la boucle



# Exercice 5 : Écrire une list comprehension qui prend une liste de nombres et retourne leurs carrés
carrés = [x ** 2 for x in range (0,25,2)]
print(carrés)





