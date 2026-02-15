import random
from personnage import Personnage

class Archer(Personnage):
    """Cette classe represente un archer

    Args:
        Personnage (class): la classe parent de Archer
    """
    def __init__(self, nom : str, vie :int, attaque : int, armure :object, vie_max : int, dexterite :int):
        super().__init__(nom, vie, attaque, armure, vie_max)

        self._dexterite = 0
        self.dexterite = dexterite


    @property
    def dexterite(self) -> int:
        return self._dexterite
    
    @dexterite.setter 
    def dexterite(self, nouvelle_dexterite : int) -> None:
        if nouvelle_dexterite >= 40 and nouvelle_dexterite <= 70:
            self._dexterite = nouvelle_dexterite
        elif nouvelle_dexterite < 40:
            self._dexterite = 40
        elif nouvelle_dexterite > 70:
            self._dexterite = 70


    #methodes
    def attaquer(self) -> int:
        """calcul les degats de l'attaque de l'archer

        Returns:
            int: les degats de l'attaque
        """
        bonus  = random.randint(0,100)
        degats = 0
        if bonus < self.dexterite:
            degats = int((self.attaque + 15) * 2)
        else :
            degats = int(self.attaque + 15)

        return degats   

    def __str__(self):
        return f"Archer {self.nom}, pv : {self.vie}, Attaque : {self.attaque} Dexterité : {self.dexterite}"