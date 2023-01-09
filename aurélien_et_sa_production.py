# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 19:42:59 2023

@author: Aurélien
"""

identification = "\n\Pouvez vous nous indiquez votre nom et prénom ? "

identification = input ("\n\Pouvez vous nous indiquez votre nom et prénom ? ")
if identification == #nom d'un client
    mot_de_passe = input ("\n\Veuillez entrer votre mot de passe: ")
    if mot_de_passe == #mdp du client en question
    statut = "client "
    else:
        pass
elif identification == #nom d'un conseiller
    mot_de_passe = input ("\n\Veuillez entrer votre mot de passe: ")
    if mot_de_passe == #mdp du conseiller en question
    statut = "conseiller "
    else:
        pass
else:
    identification_erronee = input ("\n\Merci de réinsérer votre nom et prénom : ")
    #Faire une fonction pour relancer le programme