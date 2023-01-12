from data_3 import (text_intro,text_for_action_for_clients, \
                    text_for_action_for_advisor,text_action_withdrawal,\
                    text_action_deposit, text_action_history)

import json
 ############################################################################################################################
list_name_advice = {"Hellie Trop","Noah Brzezinski","Batarde Patrop","Iris Machina", \
                    "Jean Pranote","Henri Gluant","Jesus Pauvre","Tom Desavoie", "Lamadre Dekanté" \
                    "Pika Pikachu","Tessie Drole","Sam Minèreve"}
list_name_advisor = {"Monsieur Patate","Océane Ho"}

replay_commands = \
    ["y", "yes", "Y", "go", "ok", "Yes", "on y va", "let's go", "oui", "o", "O", "Oui"]





def action_list_advice_advisor ():
    text_list_advice = ("Voici la liste des clients qui ont été enregistrés dans notre base de données client :" \
                        + str (list_name_advice))
    return text_list_advice


#############################################################################################################################




def identification_fct(name):
    statut = input("Quel est votre statut ? ")
    if statut == "client":
        if name not in list_name_advice :
            identification_erronee()
        else:
            statut = "client"
            return statut
            
    
    if statut == "conseiller":
        if name not in list_name_advisor :
            identification_erronee()
        else:
            statut = "conseiller"
            return statut
            

def mot_de_passe_fct():
    mot_de_passe = input ("\nVeuillez entrer votre mot de passe: ")
    with open ("dico.json","r") as file:
        dico = json.loads(file)
        if mot_de_passe != dico([name]["mot_de_passe"]) :
           password_false()
            
        else:
           print ("mot de passe valide")
          
def identification_erronee():      
    print ("\nVotre identifiant est incorrect.\n\n")
    return identification_fct()

def password_false():
    print("votre mot de passe est invalide")
    new_try = identification_fct()
    return (new_try)
#####################################################################################################################################

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


####################################################################################################################################


def restart_advice ():
    play = "yes"
    while play in replay_commands:
        menu_for_clients()
        play = input ("Voulez vous encore bénéficier de nos services ?")


def restart_advisor ():
    play = "yes"
    while play in replay_commands:
        menu_for_advisor()
        play = input ("Voulez vous encore bénéficier de nos services ?")
####################################################################################################################################


def menu_for_clients():
    print (text_for_action_for_clients)
    action = int(input("Quel est votre action ?"))
    if action == 1:
        return action_account(name)
    if action == 2:
        print (text_action_withdrawal)
        amount = int(input("montant :"))
        return amount
    if action == 3:
        print (text_action_deposit)
        deposit = int(input("dépot : "))
        return deposit
    if action == 4:
        print(text_action_history)

def menu_for_advisor ():
    print (text_for_action_for_advisor)
    action = int(input("Quel est votre action ?"))
    if action == 0:
        action_list_advice_advisor()
    if action == 1:
        return action_account(name)
    if action == 2:
        print (text_action_withdrawal)
        amount = int(input("montant du retrait :"))
        return amount
    if action == 3:
        print (text_action_deposit)
        deposit = int(input("montant du dépot : "))
        return deposit
    if action == 4:
        print(text_action_history)

####################################################################################################################################
intro = print(text_intro)
name = input ("\nPouvez vous nous indiquez votre nom et prénom ? ")
statut = identification_fct(name)
mot_de_passe = mot_de_passe_fct()
if statut == "client":
    restart_advice()

if statut == "conseiller ":
    restart_advisor()


