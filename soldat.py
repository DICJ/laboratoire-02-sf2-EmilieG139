from personnage import Personnage

class Soldat(Personnage):
    """represente le personnage d'un soldat

    Args:
        Personnage (class): classe parent du personnage
    """

    def __init__(self, nom : str, vie :int, attaque : int, armure : object, vie_max : int):
        super().__init__(nom, vie, attaque, armure, vie_max)

    
    def subir_degats(self, degats : int) -> None:
        """permet de calculer les degats infliger au soldat selon son armure

        Args:
            degats (int): les degats infligés par l'attque de l'autre personnage
        """
        degats_final = degats - self.armure.points_armure
        if degats_final < 0:
            degats_final = 0

        degats_final = degats_final * 0.9
        self.vie -= degats_final

    def __str__(self):
        return f"Soldat {self.nom}, pv : {self.vie}, Attaque : {self.attaque}"