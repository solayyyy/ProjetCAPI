import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

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
