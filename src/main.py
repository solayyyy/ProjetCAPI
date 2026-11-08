import sys
from Models import Backlog
from src.cli import saisir_joueurs



def main() -> None:
   
    joueurs = saisir_joueurs()

       # Chargement backlog (US-07)
    try:
        backlog = Backlog.charger_depuis_fichier("exemples/backlog.json")
    except Exception as err:
        print(f"Erreur lors du chargement du backlog : {err}", file=sys.stderr)
        sys.exit(1)

    print(f"Projet actif : {backlog.projet}")

  

if __name__ == "__main__":
    main()
