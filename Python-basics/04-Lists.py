# HelloWorld - 22 avril 2026



# Lists : structures mutables pour stocker une collection d'éléments, définies avec [] et séparées par des virgules.
## Création d'une liste
genes = ["BRCA1", "BRCA2", "TP53", "EGFR", "MYC"]  # Liste de 5 gènes
print(genes)
mixte = ["Chelsea", 24, 1.60, True]  # Types mixtes : str, int, float, bool
vide = []  # Liste vide


## Accès aux éléments d'une liste par leur index
print(genes[0])  # Index 0: premier élément
print(genes[2])  # Index 2: troisième élément
print(genes[-1])  # Index -1: dernier élément
print(genes[-2])  # Index -2: avant-dernier élément
print(mixte[1])  # Index 1: deuxième élément


## Slicing : extrait une partie de la liste avec la syntaxe liste[début:fin] (fin exclus)
print(genes[1:4])  # Index 1 à 3: ['BRCA2', 'TP53', 'EGFR']
print(genes[:3])  # Du début à 2: ['BRCA1', 'BRCA2', 'TP53']
print(genes[2:])  # À partir de 2: ['TP53', 'EGFR', 'MYC']
print(genes[::2])  # Un élément sur deux: ['BRCA1', 'TP53', 'MYC']
print(genes[-2:])  # Les 2 derniers: ['EGFR', 'MYC']
print(genes[:-1])  # Tous sauf le dernier
print(genes[::-1])  # Inversé: ['MYC', 'EGFR', 'TP53', 'BRCA2', 'BRCA1']
print(genes[1:4:2])  # Index 1-3, pas 2: ['BRCA2', 'EGFR']
print(genes[-1:])  # Le dernier: ['MYC']


# Manipulation des listes : méthodes pour ajouter, supprimer, trier, etc.
genes = ["BRCA1", "BRCA2", "TP53"]

## Ajouter un élément à la fin de la liste
genes.append("EGFR")  # Ajoute un élément à la fin
genes.extend(["MYC", "MLH1"])  # Ajoute plusieurs éléments à la fin
genes.insert(1, "MLH1")  # Insère un élément à une position spécifique

## Supprimer un élément de la liste
genes.remove("BRCA2")  # Supprime la première occurrence
del genes[0]  # Supprime l'élément à l'index 0
dernier = genes.pop()  # Supprime et retourne le dernier élément
genes.pop(0)  # Supprime et retourne l'élément à l'index 0
genes.clear()  # Supprime tous les éléments

## Informations sur la liste
print(len(genes))  # Nombre d'éléments
print(genes.count("TP53"))  # Compte les occurrences
# print(genes.index("TP53"))  # Trouve l'index (génère une erreur si absent)
genes.sort()  # Trie alphabétiquement (types homogènes)
genes.reverse()  # Inverse l'ordre

## Tri
notes = [15, 2, 9, 8, 12]
notes.sort()  # Ordre croissant
print(notes)  # [2, 8, 9, 12, 15]

notes.sort(reverse=True)  # Ordre décroissant
print(notes)  # [15, 12, 9, 8, 2]

## Concaténation de listes
liste1 = ["A", "B", "C"]
liste2 = ["D", "E", "F"]
liste_concaténée = liste1 + liste2  # Crée une nouvelle liste (ne modifie pas les originales)
print(liste_concaténée)  # ['A', 'B', 'C', 'D', 'E', 'F']
# Ou: liste1.extend(liste2) pour modifier liste1 directement



# Listes 2D (Matrices) : listes imbriquées pour créer des structures plus complexes
## Matrice de données patients
patients = [
    ["Alice", 34, "F", "Oncologie"],
    ["Bob", 52, "M", "Cardiologie"],
    ["Cléo", 28, "M", "Hématologie"]
]

## Accéder à la liste : [ligne][colonne]
print(patients)  # Liste complète
print(patients[0])  # 1ère sous-liste
print(patients[1][0])  # "Bob" (ligne 1, colonne 0)
print(patients[2][3])  # "Hématologie" (ligne 2, colonne 3)

## Modification
patients[0][1] = 35  # Modifie l'âge d'Alice
print(patients[0][1])



# Exercice combiné: 
## 1 : Créer une liste de 5 maladies génétiques.
maladies_génétiques = ["Mucoviscidose", "Drépanocytose", "Neurofibromatose de type 1", "Trisomie 21", "Myopathie de Duchenne"]

## 2 : Affiche le premier, le dernier, et l'avant-dernier élément de la liste.
print(maladies_génétiques[0], maladies_génétiques[-1], maladies_génétiques[-2])

## 3 : Ajouter 2 maladies avec append() et une avec insert() à l'index 2.
maladies_génétiques.append("Hémophilie")
maladies_génétiques.append("Syndrome de l'X fragile")
maladies_génétiques.insert(2, "Phénylcétonurie") # La nouvelle liste est : ['Mucoviscidose', 'Drépanocytose', 'Phénylcétonurie', 'Neurofibromatose de type 1', 'Trisomie 21', 'Myopathie de Duchenne', 'Hémophilie', "Syndrome de l'X fragile"].

## 4 :  Utiliser le slicing pour afficher les 3 premières et les 2 dernières.
print(maladies_génétiques[:3])
print(maladies_génétiques[-2:])

## 5 : Liste 2D de gènes avec chromosome et fonction
liste_genes = [
    ["BRCA1", 17, "Suppresseur de tumeur et réparation de l'ADN"], # Bien penser à mettre la virgule après les sous-listes, sauf après la derniière.
    ["TP53", 17, "Suppresseur de tumeur et contrôle du cycle cellulaire"],
    ["EGFR", 7, "Récepteur de facteur de croissance épidermique"]
]

## 6 : Affiche et trie la liste
print(liste_genes)
liste_genes.sort()
print(liste_genes) 



