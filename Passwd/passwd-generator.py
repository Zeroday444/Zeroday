import random
import string

# Fonction pour générer un mot de passe complexe
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Entrées utilisateur
NAME = input("Enter the name: ")
SECOND_NAME = input("Enter the second name: ")
SURNAME = input("Enter the surname: ")
AGE = input("Enter the age: ")
FAVORITE_NUMBER = input("Enter the favorite number: ")
CITY = input("Enter the city: ")
CODE_CITY = input("Enter the code city: ")
EMAIL = input("Enter the email: ")

# Génération des mots de passe en combinant les informations utilisateur
passwords = [
    f"{NAME}{AGE}{generate_password(4)}",
    f"{NAME}{SECOND_NAME}{generate_password(4)}",
    f"{NAME}{SURNAME}{generate_password(4)}",
    f"{NAME}{FAVORITE_NUMBER}{generate_password(4)}",
    f"{NAME}{CODE_CITY}{generate_password(4)}",
    f"{NAME}{CITY}{generate_password(4)}",
    f"{NAME}{EMAIL.split('@')[0]}{generate_password(4)}"
]

# Impression et enregistrement des mots de passe générés
password_file = '/home/zeroday/Tools/passwd/password.txt'

with open(password_file, 'w') as file:
    for pwd in passwords:
        print(pwd)
        file.write(pwd + '\n')

print("Passwords generated and saved to", password_file)
