compteur = 0
valeur_recherchee = ""
#valeur_recherchee = int(valeur_recherchee)
valeur_max = 10
trouve = False

# if not isinstance(valeur_recherchee, int):
inputOk = False
while inputOk == False:
    valeur_recherchee = input('Insert number here: ')
    if isinstance(valeur_recherchee, int):
        inputOk = True
    else:
        print("This is not a number, please insert a number.")
while compteur < valeur_max:
    if compteur == int(valeur_recherchee):
        print("valeur trouvée")
        trouve = True
        break
    compteur = compteur + 1

if not trouve:
    print("La valeur n'a pas été trouvée")
