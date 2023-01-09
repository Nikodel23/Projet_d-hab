






nom = input("Quel est son nom : ")
date_de_naissance = input("Quel est ta date de naissance : ")
mot_de_passe = input("Quel est son mot de passe :")
compteur = input("Combien il y a dans son compte initialement : ")

text_dico =\
("\n    \"")+(nom)+("\": [") + \
("\n        {") + \
("\n            \"date de naissance\": \"") +(date_de_naissance)+("\",") +\
("\n            \"mot de passe\: \"") + (mot_de_passe) + ("\",")+\
("\n            \"compteur\":")+ (compteur)+ (",")+\
("\n        },") +\
("\n        {") + \
("\n            \"historique\" :{}") + \
("\n        }]")


print(text_dico)
 
 
dico_information = \
{
    "Hellie Trop": [
        {
            "date de naissance": "12/13/10",
            "mot de passe": "voleràlamaison",
            "compteur": 1908
        },
        {
            "historique" :{}
        }]
}
