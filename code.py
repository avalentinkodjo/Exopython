    # tableau etudiant
etudiant= []
nbetudiant=5
nbmatiere=5
for i in range (nbetudiant):
    print("etudiant:" , i+1)
    nom = input("entrer votre nom : ")
    somme = 0
    for j in range (nbmatiere):

        note = float(input("entrer votre note : "))
        somme = somme + note
        print(f"entrer la note de la matiere : {j+1} ")
        moyenne = somme / nbmatiere
        print("votre moyenne est : ", moyenne)
        etudiant.append([nom,moyenne])
        






