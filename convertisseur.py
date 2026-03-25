class ServiceTauxDeChange:
    def obtenir_taux(self, devise_source: str, devise_cible: str) -> float:
        """
        Simule l'obtention du taux de change entre deux devises.

        Par exemple, pour convertir de l'USD à l'EUR, on pourrait retourner un taux de 0.85.
        obtenir_taux("USD", "EUR") -> 0.85

        """
        raise NotImplementedError("API de taux de change indisponible")


class Convertisseur:
    def convertir(
        self,
        montant: float,
        devise_source: str,
        devise_cible: str,
        service_taux: ServiceTauxDeChange,
    ) -> float:
        taux: float = service_taux.obtenir_taux(devise_source, devise_cible)
        return round(montant * taux, 2)
