from data_3 import (text_intro,text_for_action_for_clients, \
                    text_for_action_for_advisor,text_action_withdrawal,\
                    text_action_deposit, text_action_history, \
                    text_action_account)

#identifier la personne
intro = print(text_intro)
statut = "client"
if statut == "client":
    def menu_for_clients():
        print (text_for_action_for_clients)
        action = int(input("Quel est votre action ?"))
        if action == 1:
            print(text_action_account)
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

print (menu_for_clients())
  


if statut == "conseiller ":
    def menu_for_advisor ():
        print (text_for_action_for_advisor)
        action = int(input("Quel est votre action ?"))
        if action == 0:
            pass
        if action == 1:
            print(text_action_account)
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
        
        
    