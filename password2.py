
# avec regex

import re

mot_de_passe = "MotDePasse@123"

regex = r'^(?=.*[A-Z])(?=.*[!@#$%^&*()\-_+=\[\]{}|;:\'",.<>?/\\]).{9,}$'
    
if re.match(regex, mot_de_passe):
    print("Mot de passe valide")
else:
    print("Mot de passe invalide")
