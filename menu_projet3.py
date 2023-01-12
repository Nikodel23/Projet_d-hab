from data_3 import (text_intro,text_for_action_for_clients, \
                    text_for_action_for_advisor,text_action_withdrawal,\
                    text_action_deposit, text_action_history, \
                    list_name_advice,list_name_advisor,replay_commands)

import json

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
        if mot_de_passe != dico[name]["mot_de_passe"]:
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
    mdp = dico[name]["mot de passe"]
    compteur = dico [name]["compteur"]
    date_birth = dico [name]["date de naissance"]
    texte_action_account = ("Votre compte comprends les informations suivantes :\n" \
    +"\n Nom : " + str (name) \
    +"\n Date de naissance : " + str (date_birth) \
    +"\n Mot de passe : " + str (mdp) \
    +"\n Solde restante : " + str (compteur))
    print (texte_action_account)


def text_historique (name):
    with open ("dico.json","r") as file:
        dico = json.load(file)
    historique = dico[name]["historique"]
    print (historique)
    return historique

def write_in_json_file_dico_python (dico, json_file_name):
    with open (json_file_name, 'w') as file:
        json.dump (dico, file)


def action_deposit (name):
    deposit = int(input("montant de votre dépot : "))
    with open ("dico.json","w") as file:
        dico = json.loads(file)
        solde_nouvelle = dico[name]["compteur"] 
        solde_nouvelle += deposit
        print(dico[name]["compteur"][solde_nouvelle])
        write_in_json_file_dico_python(dico[name]["compteur"][solde_nouvelle], dico.json)
        print (dico[name]["compteur"])
        
def action_withdrawal (name):
    amount = int(input("montant de votre retrait : "))
    with open ("dico.json","w") as file:
        dico = json.loads(file)
    if amount >= dico[name]["compteur"]:
        return ("error 404")
    else:
        solde_nouvelle = dico[name]["compteur"] 
        solde_nouvelle -= amount
        write_in_json_file_dico_python(dico[name]["compteur"][solde_nouvelle], dico.json)
        print (dico[name]["compteur"])

def action_list_advice_advisor ():
    text_list_advice = ("Voici la liste des clients qui ont été enregistrés dans notre base de données client :" \
                        + str (list_name_advice))
    return text_list_advice

####################################################################################################################################


def restart_advice ():
    play = "yes"
    while play in replay_commands:
        menu_for_clients()
        play = input ("\n\\n Voulez vous encore bénéficier de nos services ?")


def restart_advisor ():
    play = "yes"
    while play in replay_commands:
        menu_for_advisor()
        play = input ("\n\\n Voulez vous encore bénéficier de nos services ?")
####################################################################################################################################


def menu_for_clients():
    print (text_for_action_for_clients)
    action = int(input("Quel est votre action ?"))
    if action == 1:
        return action_account(name)
    if action == 2:
        print (text_action_withdrawal)
        action_withdrawal(name)
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
        action_account(name)
    if action == 2:
        print (text_action_withdrawal)
        action_withdrawal(name)
    if action == 3:
        print (text_action_deposit)
        action_deposit(name)
    if action == 4:
        print(text_action_history)

####################################################################################################################################
intro = print(text_intro)
name = input ("\nPouvez vous nous indiquez votre nom et prénom ? ")
statut = identification_fct(name)
#mot_de_passe = mot_de_passe_fct()
if statut == "client":
    restart_advice()
if statut == "conseiller ":
    restart_advisor()


