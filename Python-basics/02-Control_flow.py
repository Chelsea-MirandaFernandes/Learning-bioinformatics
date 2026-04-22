# HelloWorld - 13 avril 2026



# Valeurs booléennes : True ou False.
is_true = True
is_false = False

print(type(is_true))  # <class 'bool'>



# Instructions if : exécuter du code basé sur une condition booléenne.
test_value = 100

if test_value > 1: # ":" permet d'indenter.
    print("This code is executed !")

if test_value > 1000 :
    # Si l'expression évalue à "False", alors l'expression est sautée et le programme exécute la prochaine ligne de code indenté au même niveau que "if".
    print ("This code is NOT excuted !")

print("Program continues at this point.") 



# Instructions elif : continuer les vérifications après if
pet_type = "fish"

if pet_type == "dog": 
    print("You have a dog.")
elif pet_type == "cat": # "elif" : contraction de "else if", permet de vérifier une condition supplémentaire si les conditions précédentes sont False.
    print("You have a cat.")
elif pet_type == "fish": # Ne pas indenter "elif" sous "if", sinon il ne sera vérifié que si "if" est True.
    print("You have a fish.")



# Instructions else : exécuter un code alternatif si if est False
test_value = 50

if test_value < 1:
    print("Value is < 1.")
else:
    print("Value is >= 1.")



## Exemple if/elif/else
note = 14

if note >= 16:
    print("Very good !") # Exécuté si note >= 16
elif note >= 12:
    print("Good !") # Exécuté si note >= 12
elif note >= 10:
    print("Sufficient !") 
else:
    print("Not sufficient !") # Exécuté dans tous les autres cas



# Opérateurs de comparaison
a = 10
b = 20

print(a == b)  # False - égal
print(a != b)  # True - différent
print(a < b)   # True - inférieur
print(a > b)   # False - supérieur
print(a <= b)  # True - inférieur ou égal
print(a >= b)  # False - supérieur ou égal

## "==" compare / "=" assigne
x = 5  # Assigne
x == 5  # Compare - retourne True



# Opérateurs logiques
## "and" : True si LES 2 sont True
print(True and True)    # True
print(True and False)   # False
print(1 == 1 and 1 < 2)  # True
print(1 < 2 and 3 < 1)   # False

## "or" : True si AU MOINS 1 est True
print(True or False)    # True
print(False or False)   # False

## "not" : inverse la valeur
print(not True)    # False
print(not False)   # True

if "Yes" != "No":
    print("They are NOT equal.")

val_1 = 10
val_2 = 20

if val_1 != val_2:
    print("They are NOT equal.")

if (10 > 1) != (10 > 1000):
    print("They are NOT equal.")

## Exemple combiné
age = 24
student = True

if age >= 18 and student:
    print("The student is a major.")



# Exercice 1 : Catégoriser la température (hypothermie, normale, fièvre) avec if/elif/else
temperature = 37.5

if temperature < 36.0:
    print("Hypothermie.")
elif 36.0 <= temperature <= 37.5:
    print("Normale.")
else:
    print("Fièvre.")



# Exercice 2 - Créer 2 variables booléennes et tester les opérateurs and/or/not.
is_true = True
is_false = False

marie_age = 17
fanny_age = 26

print("Test AND :", is_true and marie_age < fanny_age)
print("Test OR :", marie_age > 20 or fanny_age > 20)
print("Test NOT :", not is_true)



# Exercice 3 : Vérifier si une note est entre 10 et 20 en utilisant "and"
note = 13

print("Test AND :", note >= 10 and note <= 20)
print(10 <= note <= 20)  # Syntaxe préférée (plus proche des mathématiques)