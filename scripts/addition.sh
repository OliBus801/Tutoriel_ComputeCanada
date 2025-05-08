#!/bin/bash
#SBATCH --output=logs/resultat_%j.out       # Fichier de sortie
#SBATCH --time=00:30:00                        # Temps d'exécution (hh:mm:ss)
#SBATCH --gpus-per-task=0                      # Configuration GPU
#SBATCH --mem-per-cpu=10000M                   # Mémoire par CPU

# Charger les modules nécessaires
module load python 

# Charger l'environnement virtuel
source ENV/bin/activate

# Commandes à exécuter
echo "Début du job"
sleep 15
python addition.py
echo "Fin du job"