# Créé par Eleve, le 27/12/2021 en Python 3.7
from file import *
import time, random, graphics

class Projet_final:

    def __init__(self):
        pass

    def start(self):
        # Creer une animation
        animation = Animation(3)

        # Creer un péage avec 3 files
        peage = Peage("Saint-Arnoult",3)

        while True:
            # Temporisation
            time.sleep(2)
            # Creer voiture
            voiture = Voiture(animation, couleur = random.choice([graphics.rouge, graphics.jaune, graphics.vert, graphics.bleu]))
            # Ajouter voiture dans péage
            peage.ajouter(voiture)
            # Vérifier l'état des files
            peage.verifier_files(animation)


class Peage:

    def __init__(self,nom,nombre_de_files):
        self._nom = nom
        self._nombre_de_files = nombre_de_files
        self._files = [File() for i in range(nombre_de_files)]

    def comparer_files(self):
        nb_elts = 99
        for i, j in enumerate(self._files):
            if j.est_vide() == True:
                nb_elts = 0
                numero_de_file = i
                file = j
                continue
            if j.nb_elts() < nb_elts:
                nb_elts = j.nb_elts()
                numero_de_file = i
                file = j

        print(f"La file {numero_de_file} est choisie car elle contient {nb_elts} voiture(s)")
        return numero_de_file, file


    def ajouter(self,voiture):
        """ A COMMENTER """
        numero_de_file, file_a_utiliser = self.comparer_files()
        print(f"Ajout d'une voiture sur la file {numero_de_file}")
        file_a_utiliser.ajouter(voiture)

        # La voiture n'est pas première donc elle attends
        # Je suis en première position
        if file_a_utiliser.nb_elts() == 1:
            print("La voiture est en première position")
            if voiture.temps_ecoule() == True:
                print(f"Le temps est écoulé, la voiture disparaît")
                file_a_utiliser.retirer()
            else:
                print("Il reste du temps, la voiture reste là")
                pass
        # La voiture n'est pas première donc elle attends
        else:
            print("La voiture n'est pas en première position")
            pass


    def verifier_files(self,animation):
        """ A COMMENTER """
        print(f"On vérifie les files pour afficher les voitures")
        for numero_de_file, file in enumerate(self._files):
            print(f"On vérifie la file {numero_de_file}")

            if file.est_vide() == True:
                print(f"La file {numero_de_file} est vide")
                continue
            else:
                voiture = file.tete.val
                print(f"La voiture {voiture} est en tête de file")
                if voiture.temps_ecoule() == True:
                    # Gestion de File
                    file.retirer()
                    print(f"Le temps est écoulé pour la voiture, on la retire")
                else:
                    print(f"Il reste du temps pour la voiture, elle reste au péage")

            nb_elts = 0

            if file.est_vide() == True:
                nb_elts = 0
            else:
                nb_elts = file.nb_elts()

            print(f"La file {numero_de_file} contient {nb_elts} voitures")

            for position in range (0, nb_elts):
                print(f"Voiture en position {position}")
                voiture = file.tete.val
                # On n'affiche pas la voiture au dessus
                if position <= 4:
                    print("On dessine la voiture")
                    voiture.afficher(numero_de_file,position)
                else:
                    # On n'affiche plus la voiture car elle est trop loin
                    print("On ne dessine pas la voiture")

                # On retire la voiture de la position 1 et on là met à la fin
                file.retirer()
                file.ajouter(voiture)

            # Nombre maximum de voiture (4) qui sont par file
            for position_vide in range(nb_elts, 4):
                print(f"On efface la voiture en position {position_vide}")
                voiture = Voiture(animation,graphics.gris)
                voiture.afficher(numero_de_file,position_vide)


class Voiture:

    def __init__(self,animation,couleur = graphics.rouge):
        self._couleur = couleur
        self._animation = animation

    def temps_ecoule(self):
        time.sleep(0.5)
        # Le pourcentage est de 25 % pour vrai et 75 % pour faux
        return random.choice([True, False, False, False])

    def afficher(self,numero_de_file,position):
        self._animation.dessiner(numero_de_file,self._couleur,position)


class Animation:

    def __init__(self,nombre_de_files):
        self._nombre_de_files = nombre_de_files
        self._fenetre = graphics.init_graphics(800,650)
        self.creer_fond()
        self.creer_files(nombre_de_files)

    def creer_fond(self):
        p1 = (0,0)
        p2 = (800,650)
        graphics.draw_fill_rectangle(p1,p2,graphics.gris,self._fenetre)

    def creer_files(self,nombre_de_files):
        for numero_de_file in range(nombre_de_files):
            p1 = (0,100+105*numero_de_file)
            p2 = (800,105+105*numero_de_file)
            graphics.draw_fill_rectangle(p1,p2,graphics.blanc,self._fenetre)

    def dessiner(self,numero_de_file,couleur,position):
        p1 = (10+100*position,30+105*numero_de_file - 1)
        p2 = (90+100*position,70+105*numero_de_file - 1)
        print(f"p1 et p2 {p1},{p2},{couleur}")
        graphics.draw_fill_rectangle(p1,p2,couleur,self._fenetre)


# Instancie un objet de type Projet_final
projet_final = Projet_final()

# Démarre le péage et éteint le péage
try:
    projet_final.start()
except KeyboardInterrupt:
    graphics.quit_graphics()
    print("Terminé")


