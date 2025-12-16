# Comptes disponible (nom: solde)
comptes = {
    "Justine": 9000,
    "Dieni": 7500,
    "Valentin": 1200
}

# Cadeaux disponibles
cadeaux = {
    "Montre": 1500,
    "Chaussures": 2000,
    "Téléphone": 4500,
    "Parfum": 1800
}

while True:
    print("\n  MENU PRINCIPAL ")
    print("1. Afficher les comptes")
    print("2. Afficher les cadeaux")
    print("3. Acheter un cadeau")
    print("4. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        print("\n--- LISTE DES COMPTES ---")
        for nom, solde in comptes.items():
            print(f"{nom} : {solde} F")

    elif choix == "2":
        print("\n--- LISTE DES CADEAUX ---")
        for nom, prix in cadeaux.items():
            print(f"{nom} : {prix} F")

    elif choix == "3":
        acheteur = input("Nom du compte acheteur : ")

        if acheteur not in comptes:
            print("Ce compte n'existe pas.")
            continue

        cadeau = input("Nom du cadeau : ")

        if cadeau not in cadeaux:
            print("Ce cadeau n'existe pas.")
            continue

        prix = cadeaux[cadeau]

        if comptes[acheteur] >= prix:
            comptes[acheteur] -= prix
            print(f"Achat réussi ! {cadeau} acheté pour {acheteur}.")
            print(f"Nouveau solde :  F",{comptes[acheteur]})
        else:
            print("Achat refusé : solde insuffisant.")

    elif choix == "4":
        print("Au revoir !")
        break

    else:
        print("Choix invalide, veuillez réessayer.")
