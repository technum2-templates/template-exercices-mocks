class BaseDeNotes:
    def obtenir_notes(self, etudiant):
        raise NotImplementedError("Connexion à la base de données indisponible")


class RapportScolaire:
    def __init__(self, base_de_notes):
        self.base_de_notes = base_de_notes

    def moyenne(self, etudiant):
        notes = self.base_de_notes.obtenir_notes(etudiant)
        return sum(notes) / len(notes)

    def a_reussi(self, etudiant, seuil=10):
        return self.moyenne(etudiant) >= seuil
