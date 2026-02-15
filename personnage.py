class Personnage:
    """repreésente la classe parent de tous les personnages
    """

    def __init__(self, nom : str, vie : int, attaque : int, armure : object, vie_max : int):
        self.nom = nom
        self._vie = 0
        self._attaque = 0
        self.armure  = armure
        self._vie_max = 0

        self.vie = vie
        self.attaque = attaque
        self.vie_max = vie_max

    @property
    def vie(self):
        return self._vie
    
    @vie.setter 
    def vie(self, nouvelle_vie : int):
        if nouvelle_vie >= 0 and nouvelle_vie <= 500:
            self._vie = nouvelle_vie
        elif nouvelle_vie < 0:
            self._vie = 0
        elif nouvelle_vie > 500:
            self._vie = 500

    
    @property
    def attaque(self):
        return self._attaque
    
    @attaque.setter 
    def attaque(self, nouvelle_attaque : int):
        if nouvelle_attaque >= 0 and nouvelle_attaque <= 50:
            self._attaque = nouvelle_attaque
        elif nouvelle_attaque < 0:
            self._attaque = 0
        elif nouvelle_attaque > 50:
            self._attaque = 50


    @property
    def vie_max(self):
        return self._vie_max
    
    @vie_max.setter 
    def vie_max(self, vie_max):
        self._vie_max = vie_max

    def subir_degats(self, degats : int) -> None:
        """permet d'oter les points de degats infliger sur la vie du personnage

        Args:
            degats (int): les degats de l'attaque de l'autre personnage
        """
        degats_final = degats - self.armure.points_armure
        if degats_final < 0:
            degats_final = 0
        self.vie -= degats_final


    def attaquer(self) -> None:
        """représente l'attaque de base des personnages

        Returns:
            int: les degats d'une attaque de base
        """
        degats = self.attaque
        return degats

    def reset(self) -> None:
        """permet de reset la vie d'un personnage a son maximum
        """
        self.vie = self.vie_max

    def soigner(self) -> None:
        """permet de soigner un personnage a un certain pourcentage de sa vie maximale
        """
        indice = int(input("Quel pourcentage de vie voulez vous redonner au personnage : "))
        self.vie = int(self.vie_max * (indice / 100))

    def __eq__(self, autre_perso : object) -> bool:
        """permet de voir si deux personnages sont egaux

        Args:
            autre_perso (object): le personnage a comparer

        Returns:
            bool: si les deux personnages sont identiques (True) ou non (False)
        """
        if self.nom == autre_perso.nom and self.pv == autre_perso.pv:
            return True
        else:
            return False
        
    
