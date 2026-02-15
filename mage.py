import random
from personnage import Personnage

class Mage(Personnage):
    """represente le personnage d'un mage

    Args:
        Personnage (class): classe parent du mage
    """

    def __init__(self, nom : str, vie :int, attaque : int, armure : object, vie_max : int, mana :int, mana_max : int):
        super().__init__(nom, vie, attaque, armure, vie_max)

        self._mana = 0
        self._mana_max = 0

        self.mana = mana
        self.mana_max = mana_max

    @property
    def mana(self):
        return self._mana
    
    @mana.setter 
    def mana(self, nouveau_mana : int):
        if nouveau_mana >= 0 and nouveau_mana <= 100:
            self._mana = nouveau_mana
        elif nouveau_mana < 0:
            self._mana = 0
        elif nouveau_mana > 100:
            self._mana = 100

    
    @property
    def mana_max(self):
        return self._vie_max
    
    @mana_max.setter 
    def mana_max(self, mana_max):
        self._mana_max = mana_max

    #methodes
    def diminuer_mana(self) -> None:
        """permet de calculer le mana perdu apres une attaque
        """
        moins_mana = random.randint(15, 25)
        self.mana -= moins_mana

    def attaquer(self) -> int:
        """permet de calculer les degats faits par une attaque

        Returns:
            int: les degats de l'attaque
        """
        degats = 0
        if self.mana > 0:
            degats = int(self.attaque + 60)
        elif self.mana <= 0:
            degats = self.attaque
        self.diminuer_mana()
        return degats
    
    def __str__(self):
        return f"Mage {self.nom}, pv : {self.vie}, Attaque : {self.attaque}, Niveau de mana : {self.mana}"
    
    def reset(self) -> None:
        """permet de remettre comme au depart la vie et le niveau de mana du mage
        """
        self.vie = self.vie_max
        self.mana = self.mana_max