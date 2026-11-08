import getpass
from src.models import CARTES_VALIDEES, Backlog, Fonctionnalite, SessionPoker


def saisir_joueurs() -> list[str]:
    print("=== Configuration de la session ===")
    while True:
        try:
            nb = int(input("Nombre de joueurs : ").strip())
            if nb > 0:
                break
            print("Erreur : Il faut au moins 1 joueur.")
        except ValueError:
            print("Erreur : Entrez un entier valide.")

    pseudos = []
    for i in range(1, nb + 1):
        while True:
            pseudo = input(f"Pseudo du joueur {i} : ").strip()
            if not pseudo:
                print("Le pseudo ne peut pas être vide.")
            elif pseudo in pseudos:
                print("Ce pseudo est déjà pris.")
            else:
                pseudos.append(pseudo)
                break
    return pseudos