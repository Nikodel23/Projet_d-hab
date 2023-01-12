import json
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 19:42:59 2023

@author: Aurélien
"""
list_name_advice = {"niko","Aurelienne"}
list_name_advisor = {"noah","Poutine"}
identification = "\n\Pouvez vous nous indiquez votre nom et prénom ? "


def mot_de_passe_fct():
    mot_de_passe = input ("\nVeuillez entrer votre mot de passe: ")
    return mot_de_passe

def identification_fct():
    statut = input("Quel est votre statut ? ")
    identification = input ("\nPouvez vous nous indiquez votre nom et prénom ? ")
    if statut == "client":
        if identification not in list_name_advice :
            identification_erronee()
        else:
            statut = "client"
            print (statut)
            return (statut)
    if statut == "conseiller":
        if identification not in list_name_advisor :
            identification_erronee()
        else:
            statut = "conseiller"
            print (statut)
            return (statut)

def identification_erronee():      
    print ("\nVotre identifiant est incorrect.\n\n")
    return identification_fct()


def text_historique (name):
    with open ("dico.json","r") as file:
        dico = json.load(file)
    historique = dico[name]["historique"]
    print (historique)
    return historique

def action_account (name):
    with open ("dico.json","r") as file:
        dico = json.load(file)
    nom = dico[name]
    mdp = dico[name]["mot de passe"]
    compteur = dico [name]["compteur"]
    date_birth = dico [name]["date de naissance"]
    texte_action_account = ("Votre compte comprends les informations suivantes :\n" \
    +"\n Nom : " + str (nom) \
    +"\n Date de naissance : " + str (date_birth) \
    +"\n Mot de passe : " + str (mdp) \
    +"\n Solde restante : " + str (compteur))
    print (texte_action_account)

#def write_in_historique(dico.json):
#    if new_prelevement:
#        with open (dico.json,"w") as file:
#            file.write ("historique")
#    return
    
text_historique("Monsieur Patate")
#identification_fct()
'''if mot_de_passe_fct() == "a":
    statut = "client "
    print(statut)
 mot_de_passe = input ("\nVeuillez entrer votre mot de passe: ")
 if mot_de_passe == "été gold":
     statut = "conseiller "
     print(statut)
     '''