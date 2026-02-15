class Armure:
    """
    Represente les armures des personnages
    """

    def __init__(self, nom : str, points_armure : int):

        self.nom = nom
        self._points_armure = 0

        self.points_armure = points_armure

    @property
    def points_armure(self):
        return self._points_armure
    
    @points_armure.setter 
    def points_armure(self, nouvelle_armure : int):
        if nouvelle_armure >= 0 and nouvelle_armure <= 15:
            self._points_armure = nouvelle_armure
        elif nouvelle_armure < 0:
            self._points_armure = 0
        elif nouvelle_armure > 15:
            self._points_armure = 15