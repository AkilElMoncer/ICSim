import subprocess  # Permet d'exécuter des commandes dans le shell
import re          # Permet d'utiliser des expressions régulières
import time        # Permet d'ajouter des pauses entre les commandes

# Fonction pour envoyer une commande CAN via le shell
def send_can_command(command):
    try:
        # Exécution de la commande passée en argument dans le shell
        subprocess.run(command, shell=True, check=True)
        print(f"Commande exécutée: {command}")  # Affichage de la commande 
    except subprocess.CalledProcessError as e:
        # Capture et affichage des erreurs si la commande échoue
        print(f"Erreur lors de l'exécution de la commande: {e}")

# Fonction pour lire les commandes CAN depuis un fichier log
def read_commands_from_log(filename):
    commands = []  # Liste qui va contenir les commandes extraites
    with open(filename, 'r') as file:  # Ouverture du fichier log en mode lecture
        for line in file:
            # elle extrait la séquence de caractères qui représente le message CAN en hexadécimal après vcan0 pour l'envoyer via cansend
            match = re.search(r'vcan0\s+([A-F0-9#]+)', line)
            if match:
                # Si une correspondance est trouvée, on ajoute la commande 'cansend' correspondante à la liste
                commands.append(f"cansend vcan0 {match.group(1)}")
    return commands  # Retourne la liste des commandes extraites

# Nom du fichier log à lire
log_file = 'E.log' #'A.log' 'B.log' 'C.log' 'D.log'  

# Récupération des commandes depuis le fichier log
commands = read_commands_from_log(log_file)

# Boucle pour envoyer chaque commande CAN
for command in commands:
    print(f"Exécution de la commande: {command}")  # Affichage de la commande qui va être exécutée
    send_can_command(command)  # Envoi de la commande
    time.sleep(0.1)  # Pause de 0.1 seconde entre commande pour laisser le temps à la voiture de réagir
