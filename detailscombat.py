class Detailscombat:
    """represente les informations sur les combats
    """

    def __init__(self, nom_perso1 : str, nom_perso2 : str):
        self.nom_perso1 = nom_perso1
        self.nom_perso2 = nom_perso2
        self.vainqueur = ""
        self.nombre_tours = 0


    def plus_tours(self) -> None:
        """permet de compter le nombre de tours dans un combat
        """
        self.nombre_tours += 1

    def definir_vainqueur(self, premierperso : object, deuxiemeperso : object) -> None:
        """permet de definir le vainqueur d'un combat

        Args:
            premierperso (object): premier personnage du combat
            deuxiemeperso (object): deuxieme personnage du combat
        """
        if premierperso.vie > 0:
            self.vainqueur = premierperso.nom
        elif deuxiemeperso.vie > 0:
            self.vainqueur = deuxiemeperso.nom