class BaseDeNotes:
    def obtenir_notes(self, etudiant: str) -> list[float]:
        raise NotImplementedError("Connexion à la base de données indisponible")


class RapportScolaire:
    def __init__(self, base_de_notes: BaseDeNotes) -> None:
        self.base_de_notes: BaseDeNotes = base_de_notes

    def moyenne(self, etudiant: str) -> float:
        notes = self.base_de_notes.obtenir_notes(etudiant)
        return sum(notes) / len(notes)

    def a_reussi(self, etudiant: str, seuil: float = 10) -> bool:
        return self.moyenne(etudiant) >= seuil
