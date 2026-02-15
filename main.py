from guerrier import Guerrier
from mage import Mage
from archer import Archer
from soldat import Soldat
from arene import Arene
from armure import Armure
from detailscombat import Detailscombat

def menu_pricipal() -> None:
    """permet d'afficher le menu principal
    """
    print()
    print("1. Ajouter un personnage")
    print("2. Voir les personnages dans l'arène")
    print("3. Faire combattre deux personnages")
    print("4. Soigner un personnage")
    print("5. Nettoyer l'arène")
    print("6. Voir le nombre de combattants")
    print("7. Battle royal")
    print("8. Quitter")

    
#debut du programme
choix = 1
arene1 = Arene()

#boucle pour faire le jeu
while choix != 0:
    menu_pricipal()
    choix = int(input("Entrez un nombre : "))
    print()
    
    #match case pour les differentes options
    match choix:
        case 1:
            print("-------------------")
            print("Créer un personnage")
            print("-------------------")
            print()
            #parametres communs a tous les personnages
            type = input("Quel type de personnage voulez-vous? (Guerrier, Mage, Archer ou Soldat) : ").lower()
            nouveau_nom = str(input("Entrez le nom du personnage : "))
            nouvelle_vie = int(input("Entrez la vie du personnage (entre 0 et 500) : "))
            vie_max = nouvelle_vie
            nouvelle_attaque = int(input("Entrez l'attaque du personnage (entre 0 et 50) : "))

            #ifs pour les caractéristiques uniques a chaque personnage
            if type == "guerrier":
                nouvelle_force = int(input("Entrez la force du guerrier (entre 1 et 50) : "))
                armure_guerrier = Armure("armure de plaque", 12)
                nouveau_personnage = Guerrier(nouveau_nom, nouvelle_vie, nouvelle_attaque, armure_guerrier, vie_max, nouvelle_force)
                
            elif type == "mage":
                nouveau_mana = int(input("Entrez le niveau de mana du mage (entre 0 et 100) : "))
                mana_max = nouveau_mana
                armure_mage = Armure("armure magique", 7)
                nouveau_personnage = Mage(nouveau_nom, nouvelle_vie, nouvelle_attaque, armure_mage, vie_max, nouveau_mana, mana_max)
    
            elif type == "archer":
                nouvelle_dexterite = int(input("Entrez la dexterite de l'archer (entre 40 et 70) : "))
                armure_archer = Armure("tunique de cuir", 5)
                nouveau_personnage = Archer(nouveau_nom, nouvelle_vie, nouvelle_attaque, armure_archer, vie_max, nouvelle_dexterite)

            elif type == "soldat":
                armure_soldat = Armure("Cotte de mailles", 15)
                nouveau_personnage = Soldat(nouveau_nom, nouvelle_vie, nouvelle_attaque, armure_soldat, vie_max)

            arene1.ajouter_personnage(nouveau_personnage)

        case 2:
            print("------------------------")
            print("afficher les personnages")
            print("------------------------")
            print()
            index = 0
            #boucle pour afficher chaque personnage avec son indice
            for perso in arene1.liste_personnage:
                print(f"{index}. {perso}")
                index += 1

        case 3:
            print("-----------------------------")
            print("Faire combattre 2 personnages")
            print("-----------------------------")
            print()
            nom_perso1, nom_perso2, premierperso, deuxiemeperso = arene1.choix_perso_combat()
            details = Detailscombat(nom_perso1, nom_perso2)
            arene1.combat(premierperso, deuxiemeperso, details)
            

        case 4:
            print("---------------------")
            print("Soigner un personnage")
            print("---------------------")
            print()
            index = 0
            for perso in arene1.liste_personnage:
                print(f"{index}. {perso}")
                index += 1
            choixperso = arene1.choix_perso()
            choixperso.soigner()

        case 5:
            print("--------------------")
            print("  Nettoyer l'arène")
            print("--------------------")
            print()
            arene1.nettoyer_arene()

        case 6:
            print("----------------------------------")
            print("Nombre de personnages dans l'arene")
            print("----------------------------------")
            print()
            print(f"Le nombre de combattants est de {len(arene1)}")

        case 7:
            print("--------------------")
            print("    Battle royal")
            print("--------------------")
            print()
            for perso in arene1.liste_personnage:
                perso.reset()

            while len(arene1) > 1:
                premierperso = arene1.liste_personnage[0]
                deuxiemeperso = arene1.liste_personnage[1]
                nom_perso1 = premierperso.nom
                nom_perso2 = deuxiemeperso.nom

                details = Detailscombat(nom_perso1, nom_perso2)
                arene1.combat(premierperso, deuxiemeperso, details)
                arene1.nettoyer_arene()
                print()
            
            print(f"Le gagnant est {arene1.liste_personnage[0].nom}")
            print(arene1.liste_personnage[0])


        case 8:
            #pour sortir de la boucle
            choix = 0

        case _:
            #si l'utilisateur n'entre pas une option valide
            print("choix invalide, réessayez")