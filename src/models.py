import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional
CARTES_VALIDEES = ["0", "1", "2", "3", "5", "8", "13", "20", "40", "100", "?", "cafe"]


@dataclass(frozen=True)
class Fonctionnalite:
    id: str
    titre: str

class SessionPoker:
    def __init__(self, joueurs: List[str]):
        if len(joueurs) < 1:
            raise ValueError("Il faut au moins 1 joueur pour démarrer.")
        if len(joueurs) != len(set(joueurs)):
            raise ValueError("Les pseudos des joueurs doivent être uniques.")
        self.joueurs = list(joueurs)
        self.votes_courants: Dict[str, str] = {}

    def enregistrer_vote(self, pseudo: str, carte: str) -> None:
        if pseudo not in self.joueurs:
            raise ValueError(f"Le joueur '{pseudo}' n'est pas dans la session.")
        if carte not in CARTES_VALIDEES:
            raise ValueError(f"Carte invalide : {carte}")
        self.votes_courants[pseudo] = carte

    def est_tour_complet(self) -> bool:
        return len(self.votes_courants) == len(self.joueurs)

    def reinitialiser_votes(self) -> None:
        self.votes_courants.clear()

class Backlog:
    def __init__(self, projet: str, fonctionnalites: List[Fonctionnalite]):
        if not fonctionnalites:
            raise ValueError("Le backlog doit contenir au moins une fonctionnalité.")
        self.projet = projet
        self.fonctionnalites = fonctionnalites

    @classmethod
    def charger_depuis_fichier(cls, chemin: str | Path) -> "Backlog":
        path = Path(chemin)
        if not path.is_file():
            raise FileNotFoundError(f"Fichier introuvable : {chemin}")

        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        if "fonctionnalites" not in data or not data["fonctionnalites"]:
            raise ValueError("Clé 'fonctionnalites' absente ou vide dans le JSON.")

        taches = [
            Fonctionnalite(id=item["id"], titre=item["titre"])
            for item in data["fonctionnalites"]
        ]
        return cls(projet=data.get("projet", "Sans nom"), fonctionnalites=taches)

    def premiere_fonctionnalite(self) -> Fonctionnalite:
        return self.fonctionnalites[0]
