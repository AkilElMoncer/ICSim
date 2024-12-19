# ICSim

## **Introduction**

ICSim est un simulateur de tableau de bord de véhicule conçu pour l'apprentissage et l'expérimentation des réseaux de communication CAN (Controller Area Network). Ce projet vise à offrir une introduction pratique aux concepts et à la sécurité des réseaux automobiles.

---

## **Prérequis**

### Système d'exploitation requis
- Linux (Ubuntu ou Debian recommandé)

### Outils et bibliothèques nécessaires
1. **socketcan** : Interface pour les réseaux CAN.
2. **can-utils** : Ensemble d'outils pour manipuler les données CAN.
3. **Qt** : Framework utilisé pour l'interface graphique.

### Installation des dépendances
Exécutez les commandes suivantes pour installer les outils nécessaires :
```bash
sudo apt-get update
sudo apt-get install -y can-utils qtbase5-dev libqt5widgets5
```

---

## **Installation du Projet**

1. Clonez le dépôt GitHub :
   ```bash
   git clone https://github.com/AkilElMoncer/ICSim.git
   ```
2. Accédez au répertoire du projet :
   ```bash
   cd ICSim
   ```
3. Compilez les fichiers nécessaires :
   ```bash
   make
   ```

---

## **Lancer le Simulateur**

### Étape 1 : Démarrer l'interface CAN virtuelle
Configurez une interface CAN virtuelle sur votre système Linux :
```bash
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```

### Étape 2 : Lancer ICSim
1. Démarrez le simulateur principal :
   ```bash
   ./icsim vcan0
   ```
2. Lancez le programme d'entrée (contrôleur) :
   ```bash
   ./controls vcan0
   ```

### Étape 3 : Utiliser le Simulateur
- Contrôlez les fonctions de base du tableau de bord (clignotants, phares, etc.) via le programme `controls`.
- Surveillez les messages CAN transmis à l'aide d'outils comme `candump` :
  ```bash
  candump vcan0
  ```

---
