# 30/04/2023 17:43
# python@devnas
#Prof:Almou Bassirou
#Python Cryptographie
"""Exercice 1:
Écrire un programme python qui crypte le contenu du fichier password.txt (dans le fichier fc.txt) et qui decrypte le contenu du fichier fc.txt(dans le fichier fd.txt) .
"""
#Programme :
import os # importation du module OS(Ce module fournit une façon portable d'utiliser les fonctionnalités dépendantes du système d'exploitation)
def crypto(f): #déclaration de la fonction de crytage
    if os.path.isfile(f): #Si le fichier existe
        os.system("base64 %s >fc.txt"%f) #Création du fichier crypté
crypto('/etc/password') #Répertoire de création

def decrypto(f): ##déclaration de la fonction de dérytage
    if os.path.isfile(f): #Si le fichier existe
        os.system("base64 -d %s >fd.txt"%f) #Création du fichier décrypté
decrypto('fc.txt') #Fichier à crypté

"""Remarque :
    • os.path.isfile() : La méthode en Python est utilisée pour vérifier si le chemin spécifié est un fichier régulier existant ou non. 
      Syntaxe : os.path.isfile(chemin)
    • os.system() : Exécutez la commande (une chaîne) dans un sous-shell. Ceci est implémenté en appelant la fonction C standard system()et a les mêmes limitations. 
      Syntaxe : os.system(command) 
"""