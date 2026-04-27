# HelloWorld - 27 avril 2026



# Strings : séquence de caractères immutable
## Indexing 
adn = "ATCGGCTA"
print(adn [0]) # A : le 1er caractère
print(adn [-1]) 
print(adn [2:5]) # CCGC : slicing
print(adn [:4]) # Les 4 premiers caractères

## Longueur 
print(len (adn))

## Itérer un string : affiche chaque caractère
for nucleotide in adn :
    print(nucleotide)



# Méthodes de string : 
sequence = " atcggcta "

## Casse
print(sequence.upper()) # Affiche en majuscule
print(sequence.lower()) # Affiche en minuscule
print("Hello World".title()) # Affiche en titre 

## Nettoyage 
print(sequence.strip()) # Supprime les espaces au début et à la fin 

## Recherche
adn = "ATCGGCTA"
print(adn.find("GG")) # 3 - Index de la 1ère occurence. Affiche -1 si non trouvé
print("G" in adn) # True ou False (booléen)
print(adn.count ("A")) # 2 - Nombre d'occurences
print(adn.index("GG")) # Index du pattern (erreur si non trouvé)

## Remplacement
print(adn.replace("T","U"))

## Découpage / Assemblage
csv = "gene1, gene2, gene3"
print(csv.split(",")) # ['gene1', ' gene2', ' gene3']

genes = ["BRCA1","TP53","EGFR"]
print("-".join(genes)) #BRCA1-TP53-EGFR

## Vérifier le début et la fin
print(adn.startswith("AT"))    # True
print(adn.endswith("TA"))      # True

## Vérifier le type de caractères
print(adn.isupper())           # True (tout en majuscule)
print(adn.islower())           # False
print("123".isdigit())         # True
print("abc123".isalnum())      # True (alphanumérique)

## Trouver avec index (erreur si non trouvé, contrairement à find)
print(adn.index("GG"))         # 3
# print(adn.index("XX"))       # Erreur ValueError

## Capitaliser
print(adn.capitalize())        # "Atcggcta" (1ère lettre majuscule)
print("hello world".title())   # "Hello World"

## Multiplication de strings
adn_motif = "AT"
print(adn_motif * 3) # "ATATAT"
print("=" * 20) # Barre de séparation



# Concaténation et f-strings (pour insérer des variables dans du texte)
prénom = "Chelsea"
age = 24
IMC = 21.25

## Concaténation classique
print("Nom : " + prénom + ",age : " + str(age))

## f-string : préfixe f avant les guillemets
print(f"Nom : {prénom}, age : {age}")
print(f"IMC arrondi : {IMC:.2f}") # .2 : arrondir à 2 décimales
print(f"Résultat : {10 + 20}")



# Caractères d'échappement
print("Ligne 1\nLigne 2") # \n : nouvelle ligne
print("Col1\tCol2\tCol3") ## \t : tabulation
print("Chemin : C:\\Users\\Chelsea\\data") ## \\ : affiche un backslash
print("Elle a dit : \"Bonjour!\"") ## \" : affiche des guillemets

## Raw strings (r"...") : les backslash ne sont pas échappés (ne modifient pas le caractère suivant)
chemin_windows = r"C:\Users\Chelsea\data" # Utile pour les chemins de fichiers Windows ou les expressions régulières
print(chemin_windows)
regex = r"\d+@\w+\.com" # Pas besoin d'échapper les backslash
print(regex) 


# Chaînes multi-lignes (utile pour les descriptions longues)
description = """
Protéine BRCA1
Fonction : réparation de l'ADN
Localisation : noyau cellulaire
"""
print(description)



# Exercice : 
## Créer une séquence ADN : 'ATCGGTACGATCG'
ADN = "ATCGGTACGATCG"

## Afficher sa longueur, le premier et le dernier nucléotide
print(len(ADN))
print(ADN[0] + ADN [-1]) # OU : print(f"Premier : {ADN[0]}, Dernier : {ADN[-1]}")

## Compter combien de fois 'A' apparaît dans la séquence
print(ADN.count ("A"))

## Convertir la séquence en ARN (remplacer T par U)
print(ADN.replace ("T","U"))

## Utiliser split() sur la chaîne 'BRCA1:chromosome17:gène_suppresseur' pour extraire les 3 parties
chaîne = 'BRCA1:chromosome17:gène_suppresseur'
print(chaîne.split(":"))

## Afficher un résumé avec un f-string : 'La séquence de X nucléotides contient Y adénines'
print(f"La séquence de {len(ADN)} nucléotides contient {ADN.count("A")} adénines")


