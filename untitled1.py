text_intro = ("\n\
\n Bienvenue dans le dab de MOULA BANQUE, \
\n\
\n Vous pourrez ici consulter votre compte banquaire et effectué divers fonctions ")

text_identifiant = ("\n\
Veuillez entrer votre identifiant : \n")
text_mdp = ("\n\
Veuillez entrer votre mot de passe : \n")

action_for_advisor = ("\n\
Nous vennons de vérifier votre identifiant, vous êtes bien conseiller \
\nVoici les actions que vous pouvez effectuer selon le numéro que vous entrez :\
\n\
\n 1 : Consulter votre compte \
\n 2 : Effectuer un retrait sur votre compte \
\n 3 : Effectuer un dépot sur votre compte \
\n 4 : Consulter votre historique \
\n 5 : Consulter le compte bancaire de vos clients") 

from menu_projet3.py import menu_for_clients

def text_action_account(identification,mot_de_passe,solde):
    print(identification)
    print(mot_de_passe)
    print(solde)
    if text_action_account == 0:
        print(menu_for_clients)
        
        
def text_action_withdrawal(solde,somme):
            print(solde)
            if text_action_withdrawal == 0:
                print(menu_for_clients)
                if text_action_withdrawal == 1:
                    liste_de_possibilté_de_prélevement=[10,20,50,100,200,500]
                    somme = liste_de_possibilté_de_prélevement
                    solde = solde + somme
                    print(solde)



def text_action_deposit(solde,somme):
    print(solde)
    if text_action_deposit == 0:
        print(menu_for_clients)
    if text_action_deposit == 1:
        liste_de_possibilté_de_prélevement=[10,20,50,100,200,500]
        somme = liste_de_possibilté_de_prélevement
    if (somme > solde):
            print("Solde insuffisante!")
    else:
        solde = solde-somme
        print(solde)
        
        
        
def text_action_history(solde,solde_history):
            print(solde)
            print(solde_history)
            if text_action_history == 0:
                print(menu_for_clients)
    
     