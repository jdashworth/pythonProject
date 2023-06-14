import meteo
import affichage_meteo
from meteo_common import *
from meteo_utils import *

if __name__ == '__main__':

    # on définit un variable pour contenir le nom de la ville pour laquelle afficher la météo
    ville_en_cours = ""

    # on affiche l'écran d'accueil qui permet à l'utilisateur de rechercher une ville
    affichage_meteo.afficher_ecran_accueil()

    # on récupère le choix fait par l'utilisateur
    choix_utilisateur = int(input("Quel est votre choix (1 ou 2) ?> "))

    # si l'utilisateur choisit la première proposition de l'écran d'accueil, alors on lui demande
    # de saisir le nom de la ville qu'il recherche (une partie du nom suffit pour lancer la recherche)
    if choix_utilisateur == 1:

        # on récupère le texte de l'utilisateur saisie à l'écran et on le stock dans la variable choix_ville
        choix_ville = input("Quelle ville recherchez-vous ?> ")
        # on récupère le résultat de la recherche des villes et on le stock dans la variable liste_ville
        liste_villes = meteo.recherche_ville(choix_ville)
        # on vérifie si la recherche à bien renvoyé un résultat (pour ne pas travailler sur des données inexistantes et générer une erreur technique)
        if liste_villes == None:
            print("Désolé, aucune ville corespondante n'a été trouvée.")
        else:
            # si la variable existe mais que le nombre de ville est égale à zéro, on prévient l'utilisateur
            if len(liste_villes) == 0:
                print("Désolé, aucune ville corespondante n'a été trouvée.")
            else:
                # construction d'un dictionnaire pour classer les villes et permettre à l'utilisateur
                # de les sélectionner par un numéro
                choix_ville_recherche = {}
                numero_choix = 1
                for ville in liste_villes:
                    choix_ville_recherche[numero_choix] = ville
                    numero_choix += 1

                # on affiche maintenant le résultat de la recherche à l'utilisateur pour qu'il puisse choisir une ville à consulter
                affichage_meteo.afficher_liste_ville(choix_ville_recherche)

                # en fonction du choix de l'utilisateur, on récupère la ville choisie.
                # ici, petite astuce : comme on utilise un dictionnaire avec le nomde de la ville et un index, le choix de l'utilisateur est en fait
                # l'index du dictionnaire, ce qui permet de récupérer directement le nom de la ville grâce à l'index...
                ville_en_cours = choix_ville_recherche[int(input("Pour consulter la météo d'une ville, tapez son numéro dans la liste> "))]

                # on affiche maintenant les résultats, c'est à dire les infromations météos relatives à la ville choisie par l'utilisateur.
                # pour cela on utilise une fonction d'affichage en premier pour l'entête, qui permet d'obtenir les valeurs nécéssaires en fonction de la ville choisie
                affichage_meteo.afficher_en_tete(ville_en_cours, meteo.get_temperature_actuelle(ville_en_cours), meteo.get_avis_meteo_detaille(ville_en_cours))


                # l'entête est maintenant affichée pour l'utilisateur, avec les informations météos actuelles sur la ville, mais on souhaite également afficher
                # les prévisions à 7 jours.
                # pour cela on construit une liste qui va stockée les valeurs de prévisions pour les 7 prochains jours
                liste_previsions = []

                liste_previsions.append(construire_affichage_prevision_temperature(ville_en_cours, "T° jour", PREVISION_TEMPERATURE_JOUR))
                liste_previsions.append(construire_affichage_prevision_temperature(ville_en_cours, "T° min", PREVISION_TEMPERATURE_MINI))
                liste_previsions.append(construire_affichage_prevision_temperature(ville_en_cours, "T° max", PREVISION_TEMPERATURE_MAXI))
                liste_previsions.append(construire_affichage_prevision_temperature(ville_en_cours, "T° mat", PREVISION_TEMPERATURE_MATIN))
                liste_previsions.append(construire_affichage_prevision_temperature(ville_en_cours, "T° midi", PREVISION_TEMPERATURE_APRES_MIDI))
                liste_previsions.append(construire_affichage_prevision_temperature(ville_en_cours, "T° nuit", PREVISION_TEMPERATURE_NUIT))
                liste_previsions.append(construire_affichage_prevision_pression_athmospherique(ville_en_cours))
                liste_previsions.append(construire_affichage_prevision_humidite(ville_en_cours))
                liste_previsions.append(construire_affichage_prevision_vent_vitesse(ville_en_cours))
                liste_previsions.append(construire_affichage_prevision_vent_orientation(ville_en_cours))
                liste_previsions.append(construire_affichage_prevision_avis_meteo_detaille(ville_en_cours))

                # une fois qu'on a les informations en mémoire (dans la liste) pour les prévisions météo sur les 7 prochains jours,
                # on peut les afficher à l'écran avec un formatage sur les 7 prochains jours
                affichage_meteo.afficher_previsions(liste_previsions)

                # On récupère à présent l'avis météo, c'est une chaîne de caractère.
                # En fonction de sa valeur, on va afficher une image différentes à l'utilisateur
                # image = représentation sous forme de caractères présent dans une fichier
                avis_meteo_actuel = meteo.get_avis_meteo_detaille(ville_en_cours)

                if avis_meteo_actuel == STATUT_API_NUAGEUX:
                    affichage_meteo.afficher_image_meteo(STATUT_IMAGE_METEO_NUAGEUX)
                elif avis_meteo_actuel == STATUT_API_PEU_NUAGEUX:
                    affichage_meteo.afficher_image_meteo(STATUT_IMAGE_METEO_ECLAIRCIES)
                elif avis_meteo_actuel == STATUT_API_PARTIELLEMENT_NUAGEUX:
                    affichage_meteo.afficher_image_meteo(STATUT_IMAGE_METEO_ECLAIRCIES)
                elif avis_meteo_actuel == STATUT_API_CIEL_DEGAGE:
                    affichage_meteo.afficher_image_meteo(STATUT_IMAGE_METEO_SOLEIL)
                elif avis_meteo_actuel == STATUT_API_LEGERE_PLUIE:
                    affichage_meteo.afficher_image_meteo(STATUT_IMAGE_METEO_PLUIE)
                elif avis_meteo_actuel == STATUT_API_LEGERE_COUVERT:
                    affichage_meteo.afficher_image_meteo(STATUT_IMAGE_METEO_NUAGEUX)
                else:
                    print("l'image pour la prévision actuelle n'est pas configurée, pensez à mettre à jour le code")


    elif choix_utilisateur == 2:
        pass
    else:
        print("Désolé votre choix n'est pas un 1 ou 2, que souhaitez-vous faire ?")
