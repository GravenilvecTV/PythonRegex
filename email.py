import re

text = "contact22@graven.t"
pattern = r'^[a-zA-Z0-9_.-]+@[a-z]{2,}.[a-z]{2,}$'

# verifier si le texte respecte le pattern
if re.match(pattern, text):
    print("Email valide")
else:
    print("Email invalide")