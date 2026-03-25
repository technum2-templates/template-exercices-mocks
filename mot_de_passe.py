import random
import string


def generer_mot_de_passe(longueur: int = 12) -> str:
    caracteres = string.ascii_letters + string.digits
    mot_de_passe = "".join(random.choices(caracteres, k=longueur))
    return mot_de_passe


def est_mot_de_passe_fort(mot_de_passe: str) -> bool:
    a_majuscule = any(c.isupper() for c in mot_de_passe)
    a_minuscule = any(c.islower() for c in mot_de_passe)
    a_chiffre = any(c.isdigit() for c in mot_de_passe)
    assez_long = len(mot_de_passe) >= 8
    return a_majuscule and a_minuscule and a_chiffre and assez_long
