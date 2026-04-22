# HelloWorld - 20 avril 2026



# Functions : blocs de code réutilisables (principe DRY: Don't Repeat Yourself)
## Définition d'une fonction
def dire_bonjour():
    print("Bonjour !")

## Appel de la fonction
dire_bonjour ()  # Affiche "Bonjour !"
dire_bonjour ()  # Affiche "Bonjour !" à nouveau, sans avoir à réécrire le code d'impression.



# Function parameters : les fonctions peuvent prendre des paramètres pour plus de flexibilité. Paramètres = variables locales à la fonction, utilisées pour recevoir des valeurs lors de l'appel.
def dire_bonjour_a(prénom): # Argument = valeur passée à la fonction lors de l'appel, qui est assignée au paramètre correspondant.
    print("Bonjour, ", prénom, "!")

dire_bonjour_a("Chelsea")
dire_bonjour_a("Alex")

## Fonction avec plusieurs paramètres
def calculer_imc(poids, taille):
    imc = poids / taille ** 2
    print("Votre IMC est : ", imc)

calculer_imc(60, 1.60)



# Return : permet de retourner une valeur stockée pour la réutiliser.
def additionner(a, b):
    return a + b # Renvoie le résultat.

résultat = additionner(5, 3) # Stocke 8 dans résultat.
print(résultat) # Affiche 8.
print(additionner(10, 20)) # Affiche 30.

## Retourner plusieurs valeurs
def min_max(nombres):
    return min(nombres), max(nombres)

mini, maxi = min_max([3, 1, 7, 2, 9])
print("Min : ", mini, "- Max : ", maxi) # Min : 1 - Max : 9

def square_point(x, y, z):
    x_squared = x * x
    y_squared = y * y
    z_squared = z * z
    return x_squared, y_squared, z_squared



# Portée des variables : globales (accessibles partout) vs locales (accessibles uniquement dans la fonction)
a = 5  # Variable globale

def f1():
    a = 2  # Variable locale
    print(a)  # Affiche 2 (variable locale)

print(a)  # Affiche 5 (variable globale)
f1() # Affiche 2 (variable locale de f1)



# Paramètres par défaut : définir une valeur par défaut si aucun argument n'est spécifié
def dire_bonjour_a(prénom="inconnu"):
    print("Bonjour, ", prénom, "!")

def saluer(prénom, langue="français"):
    if langue == "français":
        print("Bonjour, ", prénom, "!")
    elif langue == "anglais":
        print("Hello, ", prénom, "!")
    else:
        print("Langue non prise en charge.")

saluer("Chelsea") # Affiche "Bonjour, Chelsea !" (langue par défaut)
saluer("Alex", "anglais")
saluer("Yane", "espagnol")
        


# Fonctions lambda : fonctions anonymes sur une seule ligne
carré = lambda x: x * x # Synthaxe : "lambda" + paramètres + ":" + expression
print(carré(5))

doubler = lambda x: x * 2
print(doubler(7))



# Exercice 1 : Calculer la moyenne d'une liste de notes
def calculer_moyenne(notes):
    maths = notes[0] # L'inndexation commence à 0. 
    français = notes[1]
    histoire = notes[2]
    anglais = notes[3]
    moyenne = (maths + français + histoire + anglais) / 4
    return moyenne

print(calculer_moyenne([2, 12, 15, 18]))



# Exercice 2 : Vérifier si une personne est majeure
def est_majeur(age):
    return age >= 18

print(est_majeur(20)) 



# Exercice 3 : Convertir Celsius en Fahrenheit
def convertir_celsius_fahrenheit(c):
    return c * 9 / 5 + 32

print(convertir_celsius_fahrenheit(0))
print(convertir_celsius_fahrenheit(100))



# Exercice 4 : Appeler les fonctions avec différentes valeurs
print(calculer_moyenne([10, 15, 20, 25]))
print(est_majeur(16))
print(convertir_celsius_fahrenheit(25))
