import random
from personnage import Personnage

class Guerrier(Personnage):
    """reprente le personnage d'un guerrier

    Args:
        Personnage (class): classe parent du guerrier
    """

    def __init__(self, nom : str, vie :int, attaque : int, armure : int, vie_max : int, force :int):
        super().__init__(nom, vie, attaque, armure, vie_max)

        self._force = 0

        self.force = force

    @property
    def force(self):
        return self._force
    
    @force.setter 
    def force(self, nouvelle_force : int):
        if nouvelle_force > 0 and nouvelle_force <= 50:
            self._force = nouvelle_force
        elif nouvelle_force <= 0:
            self._force = 0
        elif nouvelle_force > 50:
            self._force = 50

    #methodes
    def attaquer(self) -> int:
        """calcul les degats faits par l'attaque du guerrier

        Returns:
            int: les degats de l'attaque
        """
        degats = int(self.attaque + (self.force / 2) + (random.randint(-2, 2)))
        return degats
    
    def __str__(self):
        return f"Guerrier {self.nom}, pv : {self.vie}, Attaque : {self.attaque}, Force : {self.force}"