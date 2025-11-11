from abc import ABC, abstractmethod
class Paiement(ABC):
    def __init__(self, montant: float):
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")
        self._montant = montant

    @abstractmethod
    def payer(self) -> str:
      pass 
class CarteBancaire(Paiement):
    def __init__(self, montant: float, numero: str, cvv: str):
        super().__init__(montant)
        self._numero = numero
        self._cvv = cvv

    def payer(self) -> str:
        return f"Paiement de {self._montant}€ effectué par CarteBancaire ****{self._numero[-4:]}"

class PayPal(Paiement):
    def __init__(self, montant: float, email: str, token: str):
        super().__init__(montant)
        self._email = email
        self._token = token

    def payer(self) -> str:
        return f"Paiement de {self._montant}€ effectué via PayPal ({self._email})"

class Crypto(Paiement):
    def __init__(self, montant: float, wallet_id: str, reseau: str):
        super().__init__(montant)
        self._wallet_id = wallet_id
        self._reseau = reseau

    def payer(self) -> str:
        return f"Paiement de {self._montant}€ effectué via Crypto ({self._reseau} - {self._wallet_id})"

def traiter_paiements(paiements: list):
    for paiement in paiements:
        print(paiement.payer())

if __name__ == "__main__":
    liste_paiements = [
        CarteBancaire(60.0, "4111222233334444", "321"),
        CarteBancaire(150.0, "5500111122223333", "654"),
        PayPal(45.0, "alice@example.com", "token789"),
        PayPal(90.0, "bob@example.net", "token101"),
        Crypto(300.0, "walletXYZ123", "BTC"),
        Crypto(750.0, "walletABC789", "ETH")
    ]

    traiter_paiements(liste_paiements)