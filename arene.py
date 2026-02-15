from detailscombat import Detailscombat

class Arene:
    """
    représente l'arene comprennant tous les personnages
    """

    def __init__(self):
        self.liste_personnage = []
        self.lst_combats = []
            
    
    #methodes
    def ajouter_personnage(self, nouveau_personnage : object) -> None:
        """Permet d'ajouter le personnage créé a la liste de personnages

        Args:
            nouveau_personnage (object): nouveau personnage créé
        """
        self.liste_personnage.append(nouveau_personnage)

    def choix_perso(self) -> object:
        """Permet de choisir un personnage dans la liste

        Returns:
            object: le personnage choisi
        """
        indice = int(input("Entrez le numero du personnage : "))
        choixperso = self.liste_personnage[indice]
        return choixperso
    
    def choix_perso_combat(self):
        """choix des personnages pour faire un combat

        Returns:
            Object, str: les personnages ainsi que leur nom
        """
        numero = 0
        for perso in self.liste_personnage:
            print(f"{numero}. {perso}")
            numero += 1
        premierperso = self.choix_perso()
        deuxiemeperso = self.choix_perso()
        nom_perso1 = premierperso.nom
        nom_perso2 = deuxiemeperso.nom
        return nom_perso1, nom_perso2, premierperso, deuxiemeperso

    
    def combat(self, premierperso : object, deuxiemeperso : object, details : object)  -> None:
        """Permet de faire un combat entre deux personnages

        Args:
            premierperso (object): premier personnage dns le combat
            deuxiemeperso (object): deuxieme personnage du combat
            details (object): object de la classe details combat pour enregistrer les infos sur le combat
        """
        tour = 0

        while premierperso.vie > 0 and deuxiemeperso.vie > 0:
            
            tour += 1
            print(f"TOUR {tour}")
            degats = premierperso.attaquer()
            deuxiemeperso.subir_degats(degats)
            print(f"{premierperso.nom} inflige {degats} de dégats à {deuxiemeperso.nom}")
            if deuxiemeperso.vie <= 0:
                break
            degats = deuxiemeperso.attaquer()
            premierperso.subir_degats(degats)
            print(f"{deuxiemeperso.nom} inflige {degats} de dégats à {premierperso.nom}")
            details.plus_tours()
            print()
            
        if premierperso.vie > 0:
            print(f"{premierperso.nom} a gagné!")
            premierperso.reset()
                
        elif deuxiemeperso.vie > 0:
            print(f"{deuxiemeperso.nom} a gagné!")
            deuxiemeperso.reset()

        details.definir_vainqueur(premierperso, deuxiemeperso)
        self.lst_combats.append(details)


    def __len__(self):
        """permet d'avoir le nombre total de personnages

        Returns:
            la longueur de la liste de personnages
        """
        return len(self.liste_personnage)
    

    def nettoyer_arene(self) -> None:
        """Permet de supprimer tous les personnages avec 0 ou moins de vie
        """
        for perso in self.liste_personnage:
            if perso.vie <= 0: 
                self.liste_personnage.remove(perso)
            


                