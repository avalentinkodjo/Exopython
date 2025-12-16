# Solde initial
solde = 10000

# Code PIN initial
pin = "1960"


def menu():
    print("\n ~~ MENU TMoney ~~")
    print("1. Consulter le solde")
    print("2. Dépôt")
    print("3. Retrait")
    print("4. Transfert")
    print("5. Changer le code PIN")
    print("6. Quitter")


while True:
    menu()
    choix = input("\nChoisissez une option : ")

    # 1. Consultation
    if choix == "1":
        saisie = input("Entrez votre code PIN : ")
        if saisie == pin:
            print(f"Votre solde est : {solde} FCFA")
        else:
            print("PIN incorrect !")

    # 2. Dépôt
    elif choix == "2":
        montant = int(input("Montant à déposer : "))
        solde += montant
        print(f"Dépôt effectué. Nouveau solde : {solde} FCFA")

    # 3. Retrait
    elif choix == "3":
        saisie = input("Entrez votre code PIN : ")
        if saisie == pin:
            montant = int(input("Montant à retirer : "))
            if montant <= solde:
                solde -= montant
                print(f"Retrait validé. Nouveau solde : {solde} FCFA")
            else:
                print("Solde insuffisant !")
        else:
            print("PIN incorrect !")

    # 4. Transfert
    elif choix == "4":
        saisie = input("Entrez votre code PIN : ")
        if saisie == pin:
            numero = input("Numéro du destinataire : ")
            montant = int(input("Montant à transférer : "))
            if montant <= solde:
                solde -= montant
                print(f"Vous avez transféré {montant} FCFA à {numero}.")
                print(f"Nouveau solde : {solde} FCFA")
            else:
                print("Solde insuffisant pour le transfert !")
        else:
            print("PIN incorrect !")

    # 5. Changer PIN
    elif choix == "5":
        ancien = input("Ancien PIN : ")
        if ancien == pin:
            nouveau = input("Nouveau PIN : ")
            pin = nouveau
            print("PIN modifié avec succès.")
        else:
            print("Ancien PIN incorrect !")

    # 6. Quitter
    elif choix == "6":
        print("Merci d’avoir utilisé TMoney.")
        break

    else:
        print("Option invalide !")
