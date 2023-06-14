valeurs = [460, 680, 17, 28]
cles = [17, 13,28]

for key in cles:
    for item in valeurs:
        if item == key:
            print(key, " a été trouvé")
            break
    else:
        print(key, " n'a pas été trouvé")

chaine  = "vive le code"
for i in range(len(chaine)):
    print(str(chaine[i]))
