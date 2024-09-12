# sans regex

mot_de_passe = "MotDePasse@123"

# Vérifier si le mot de passe a au moins 9 caractères
contient_majuscule = True
if len(mot_de_passe) < 9:
    contient_majuscule = False

# Initialiser les drapeaux pour majuscule et symbole
contient_majuscule = False
contient_symbole = False

# Liste de symboles acceptés
symboles = "!@#$%^&*()-_+=[]{}|;:'\",.<>?/\\"

# Parcourir chaque caractère du mot de passe
for caractere in mot_de_passe:
    # Vérifier si c'est une majuscule
    if caractere.isupper():
        contient_majuscule = True
    # Vérifier si c'est un symbole
    if caractere in symboles:
        contient_symbole = True

# Vérifier si les deux conditions sont remplies
if contient_majuscule and contient_symbole:
    print("Mot de passe valide.")
else:
    print("Mot de passe invalide.")
