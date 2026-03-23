class ServiceTauxDeChange:
    def obtenir_taux(self, devise_source, devise_cible):
        raise NotImplementedError("API de taux de change indisponible")


class Convertisseur:
    def convertir(self, montant, devise_source, devise_cible, service_taux):
        taux = service_taux.obtenir_taux(devise_source, devise_cible)
        return round(montant * taux, 2)
