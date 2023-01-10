# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 19:42:59 2023

@author: Aurélien
"""

list_name_advice = {"niko","Aurelienne"}
list_name_advisor = {"noah","Poutine"}
identification = "\n\Pouvez vous nous indiquez votre nom et prénom ? "
list_mdp_advice = "123"
list_mdp_advisor = "234"

def mot_de_passe_fct():
    mot_de_passe = input ("\nVeuillez entrer votre mot de passe: ")
    return mot_de_passe

def mot_de_passe_erronnee():
    print ("\nVotre mot de passe est incorrect.\n\n")
    return mot_de_passe_fct()

def identification_fct():
    statut = input("Quel est votre statut ? ")
    identification = input ("\nPouvez vous nous indiquez votre nom et prénom ? ")
    if statut == "client":
        if identification not in list_name_advice :
            identification_erronee()
        else:
            statut = "client"
            print (statut)
            mot_de_passe = input ("\nVeuillez entrer votre mot de passe: ")
            if mot_de_passe not in list_mdp_advice:
                mot_de_passe_erronnee()
            else:
                print("all good t'es un bg")
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
    
    
identification_fct()
'''if mot_de_passe_fct() == "a":
    statut = "client "
    print(statut)
 mot_de_passe = input ("\nVeuillez entrer votre mot de passe: ")
 if mot_de_passe == "été gold":
     statut = "conseiller "
     print(statut)
     '''