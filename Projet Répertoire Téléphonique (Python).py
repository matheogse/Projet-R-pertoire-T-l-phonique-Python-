
#PROJET REPERTOIRE TELEPHONIQUE 
##############################################################################################################################################
#IMPORT FICHIER CSV - EN VUE D'UNE UTILISATION TOUT AU LONG DU PROGRAMME
import csv
repertoire_csv='Repertoire CSV.csv'
with open(repertoire_csv, mode="a", newline="") as fichier_csv:
    writer = csv.writer(fichier_csv)


#AFFICHER FICHIER CSV - DEFINITION PERMETTANT L'ENTREE 5 ET AINSI AFFICHER LE CONTENU DU REPERTOIRE DANS LE FICHIER CSV
def afficher_contenu_csv(nom_fichier):
    with open(repertoire_csv, mode="r") as fichier_csv:
        lecture_csv = csv.reader(fichier_csv)
        for i in lecture_csv:
            print("Informations du contact (",i[0],") :","\n","Nom :", i[0],"\n", "Numero :", i[1],"\n")


#FONCTION MENU - DEFINITION PERMETTANT L'AFFICHAGE DU MENU AVEC 6 ENTREES DISTINCTES
def menu():
    choix=int(input("---------MENU PRINCIPAL---------\n""- Entree 0 (Pour quitter le programme) \n- Entree 1 (Pour ecrire dans le repertoire) \n- Entree 2 (Pour rechercher dans le repertoire) \n- Entree 3 (Pour mettre au format internationale) \n- Entree 4 (Pour vider le repertoire) \n- Entree 5 (Pour afficher le repertoire) \n- Entree 6 (Pour supprimer un contact en particulier): \n"))
    print("--------------------------------")
    return choix



#FONCTION CONVERSION CSV/DICTIONNAIRE - DEFINITION FONDEE DANS L'OBJECTIF DE METTRE LE REPERTOIRE EN FORMAT DE DICTIONNAIRE PARCOURABLE EN PROGRAMME PYTHON
def csv_en_dictionnaire(repertoire_csv):
    repertoire_dico = {}
    with open(repertoire_csv, mode="r") as fichier_csv:
        lecture_csv = csv.reader(fichier_csv)
        for i in lecture_csv:
            if len(i) >= 2:
                nom_contact = i[0]
                numero_contact = i[1]
                repertoire_dico[nom_contact] = numero_contact
    return repertoire_dico
dictionnaire_csv = csv_en_dictionnaire(repertoire_csv)

##############################################################################################################################################
#OPTION CHOISI PREALABLEMEMENT DANS LE MENU
while True:
    choix = menu()
    #CHOIX 0 - LE CHOIX 0 PERMET DE QUITTER LE PROGRAMME EN STOPPANT LES ACTIONS EN COURS DANS LE PROGRAMME
    if choix==0:
        print()
        print("Vous avez quittez le programme !!")
        break
    #CHOIX 1 - LE CHOIX 1 PERMET D'AJOUTER UN NOUVEAU CONTACT AVEC SON NUMERO DE TELEPHONE
    elif choix==1:
        print()
        print("Vous avez selectionner l'option de creation de contacts !")
        with open(repertoire_csv, mode="a", newline="") as fichier_csv:
            ecriture_repertoire = csv.writer(fichier_csv)
            nombre_de_contacts=int(input("Combien de contacts souhaitez vous entrer ? :"))
            print()
            for i in range(1,nombre_de_contacts+1):
                prenom_du_contact=input("Quel nom attribuez vous a votre contact ? : ")
                numero_du_contact=input("Quel est le numero de telephone de votre contact ? : ")
                print()
                ecriture_repertoire.writerow([prenom_du_contact, numero_du_contact])
        print("Voici le contenu de votre repertoire :")
        print("____________________________________________________________________________________")
        afficher_contenu_csv(repertoire_csv)
        print("____________________________________________________________________________________")


    #CHOIX 2 - LE CHOIX 2 PERMET DE RECHERCHER LES COORDONNEES TELEPHONIQUE D'UN CONTACT EN PARTICULIER
    elif choix==2:
        print()
        print("Vous avez selectionnee l'option de recherche de contacts !")
        print()
        contact_recherche=input("Entree le nom du contact ou son numero, que vous recherche en respectant les espaces entre chaque nombre et preciser le format francais s'il est mit en place avec (+33):")
        with open(repertoire_csv, mode="r") as fichier_csv:
            lecture_csv = csv.reader(fichier_csv)
        if contact_recherche in dictionnaire_csv.keys():
            print("Le contact",contact_recherche,"se voit attribue le numero suivant : ",dictionnaire_csv[contact_recherche])
        elif contact_recherche in dictionnaire_csv.values():
            for nom, numero in dictionnaire_csv.items():
                        if numero == contact_recherche:
                            print("Le numero", contact_recherche, "se voit attribuer le nom suivant :", nom)
        else:
            print("Aucun contact trouve pour le nom", contact_recherche)


    #CHOIX 3 - LE CHOIX 3 PERMET DE CONVERTIT L'ENSEMBLE DES NUMERO CONTENU DANS LE REPERTOIRE AU FORMAT TELEPHONIQUE INTERNATIONAL
    elif choix==3:
        print()
        print("Vous avez selectionnee l'option de mise au format international ! ")
        print()
        with open(repertoire_csv, mode="r") as fichier_csv:
            lecture_csv = csv.reader(fichier_csv)
            liste_lignes_repertoire = list(lecture_csv)
        if len(liste_lignes_repertoire) == 0:
            print()
            print("Le fichier CSV est vide.")
        for i in liste_lignes_repertoire:
            if i[1][:3]=="+33":
                print("Le numero de", i[0], "est deja au format francais")
            else:
                for i in liste_lignes_repertoire:
                    if len(i) >= 2:
                        i[1] = "+33 " + i[1]
                    elif i[1][0] == "0":
                        i[1] = "+33" + i[1][1:]
                with open(repertoire_csv, mode="w", newline="") as fichier_csv:
                    ecriture_repertoire = csv.writer(fichier_csv)
                    ecriture_repertoire.writerows(liste_lignes_repertoire)
                print("Les numeros ont ete convertis au format francais.")
        print()
        print("Voici le contenu de votre repertoire :")
        print("____________________________________________________________________________________")
        afficher_contenu_csv(repertoire_csv)
        print("____________________________________________________________________________________")


    #CHOIX 4 - LE CHOIX 4 PERMET DE VIDER L'ENTIERETE DU CONTENU DU REPERTOIRE (SANS SUPPRIMER LE FICHIER CSV)
    elif choix==4:
        print()
        with open("Repertoire CSV.csv", mode="w", newline="") as fichier_csv:
            print("Le repertoire a ete vide.")


    #CHOIX 5 - LE CHOIX 5 PERMET D'AFFICHER LE CONTENU DU REPERTOIRE
    elif choix==5:
        with open(repertoire_csv, mode="r") as fichier_csv:
            lecture_csv = csv.reader(fichier_csv)
            liste_lignes_repertoire = list(lecture_csv)
        if len(liste_lignes_repertoire) == 0:
            print()
            print("Le fichier CSV est vide.")
        if len(liste_lignes_repertoire)>0:
            print()
            print("Voici le contenu de votre repertoire :")
            print("____________________________________________________________________________________")
            afficher_contenu_csv(repertoire_csv)
            print("____________________________________________________________________________________")


    #CHOIX 6 - LE CHOIX 6 PERMET DE SUPPRIMER UN CONTACT EN PARTICULIER
    elif choix == 6:
        print()
        print("Vous avez selectionne l'option de suppression d'un contact en particulier ! ")
        print()
        contact_a_supprimer = input("Entree le nom du contact que vous souhaitez retirer :")

        if contact_a_supprimer in dictionnaire_csv:
            dictionnaire_csv.pop(contact_a_supprimer)
            print("Le contact", contact_a_supprimer, "a bien ete efface.")
            with open(repertoire_csv, mode='w', newline='') as fichier_csv:
                writer = csv.writer(fichier_csv)
                for nom, numero in dictionnaire_csv.items():
                    writer.writerow([nom, numero])
            print()
            print("Voici le contenu de votre repertoire :")
            print("____________________________________________________________________________________")
            afficher_contenu_csv(repertoire_csv)
            print("____________________________________________________________________________________")
        else:
            print("Aucun contact trouve pour le nom", contact_a_supprimer)


    #AUCUN DES 6 CHIFFRES
    else:
        print("Veuillez entrer une valeur valide parmi celles proposee (0/1/2/3/4/5/6)")

    ##############################################################################################################################################

