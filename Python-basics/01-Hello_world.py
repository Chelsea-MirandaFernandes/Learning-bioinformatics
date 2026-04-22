# HelloWorld - 12 avril 2026



# Variables : le signe "="" est utilisé pour donner une valeur ou un texte entre "" à une variable. Il est possible de mettre à jour la valeur d'une variable après l'avoir assigné. 
name = "Chelsea" # string : texte entre guillemets. Il est possible de donner un nom à une variable en y intégrant un "_" : user_name. Cela peut être fermé par : " ou '. Pour indiquer que la string continue à la ligne suivante, on utilise "\". Par exemple, longer = "This string is broken \ over multiple lines".
age = 24 # int : nombre entier.
taille = 1.60 # float ou nombre flottant : nombre décimal.
verified = True # bool : True ou False.



# Arithmetic operations
result = 10 + 30 # L'opérateur "+"" est utilisé pour l'addition. Il peut également être utilisé pour la concaténation de chaînes de caractères. Par exemple, "Hello " + "World" donnerait "Hello World".
addition = 15 + 28
subtraction = 50 - 20
division = 16 / 4 # Pour un résultat entier, utilisez "// au lieu de "/"", sinon cela donnera un résultat flottant.
multiplication = 7 * 6 
exponentiation = 2 ** 3 # L'exponentiation élève le nombre de gauche à la puissance du nombre de droite. Donc, 2 ** 3 signifie 2 élevé à la puissance de 3, ce qui donne 8.
modulus = 10 % 3 # Le modulus donne le reste de la division de 10 par 3, qui est 1.



# Print : utilisée pour afficher un texte, un résultat ou une information. Elle accepte un ou plusieurs arguments et affiche chacun d'eux en les séparant par un espace. Si aucun argument n'est forni, la fonction print () affiche simplement une ligne vide.
print(f"Bonjour {name}, tu as {age} ans.") # f-string est une méthode de formatage de chaînes de caractères permettant d'insérer des expressions Python directement dans des chaînes de caractères en les entourant de accolades {}. Par exemple, f"Hello {name}" insérera la valeur de la variable name dans la chaîne, donnant "Hello Chelsea".
print("Le résultat de l'addition est :", result)
print("Le résultat de l'addition est :", addition)
print("Le résultat de la soustraction est :", subtraction)
print("Le résultat de la division est :", division)
print("Le résultat de la multiplication est :", multiplication)
print("Le résultat de l'exponentiation est :", exponentiation)
print("Le résultat du modulus est :", modulus) 

print(name, age) # Faire afficher plusieurs valeurs.

## "\n" est utilisé pour créer une nouvelle ligne dans une chaîne de caractères. Par exemple, "Hello\nWorld" affichera "Hello" sur la première ligne et "World" sur la deuxième ligne.
print("Hello\nWorld")   

## "\t" pour un tabulation, qui ajoute un espace de retrait dans la ligne. Par exemple, "Hello\tWorld" affichera "Hello" suivi d'une tabulation avant "World".
print("Hello\tWorld")

## Chaque print () finit par un saut de ligne. Pour que deux print () soient sur la même ligne, on peut utiliser end="" pour spécifier que le print ne doit pas ajouter de saut de ligne à la fin. Par exemple, print("Hello", end="") suivi de print("World") affichera "HelloWorld" sur la même ligne.
print("Hello", end="")
print("World") 



# Plus-equal operator
counter = 0
counter += 10 # C'est l'équivalent de : counter = counter + 10.

message = "Partie 1 du message"
message += "Partie 2 du message" # L'opérateur fera également la concaténation (l'enchaînement) des strings.



# Integers : nombre écrit sans fraction/décimale. Il peut être négatif, positif ou 0.
chairs = 4
tables = 1 
broken_chairs = -2
sofas = 0



# String concatenation 
first = "Hello"
second = "World"

result = first + second

long_result = first + second + "!"


# Errors : pour la plupart des cas d'erreur, l'interprèete affichera la ligne d code où l'erreur a été détectée et placera un accent circonflexe ^ sous la partie du code à l'origine de l'erreur.
## SyntaxError : code mal écrit, parenthèse manquante. Par exemple, age = 7 + 5 = 4.
## IdentationError : identation incorrecte.
## NameError : variable utilisée avant d'être définie. Par exemple, print (x) sachant que x est inexistant.
## ZeroDivisionError : division par zéro. Par exemple, 100/0. 