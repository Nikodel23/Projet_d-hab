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

def exit():
   pass 

n1 = input ("Voulez vous rentrer sur votre compte? ")
if n1 == "oui":
            pass
elif n1 == "non":
        print ("à la prochaine")
else :
    print ("comprends pas ")

print("n1. Consulter votre compte")
print("n2. Effectuer un retrait sur votre compte")
print("n3. Effectuer un dépot sur votre compte")
print("n4. Consulter votre historique")
print("n5. Consulter le compte bancaire de vos clients")


#print("exiting the program")
#print(quit())
