#!/bin/bash
#SBATCH --output=logs/resultat_%j.out            # Fichier de sortie
#SBATCH --time=00:30:00                     # Temps d'exécution (hh:mm:ss)
#SBATCH --gpus-per-task=0          # Configuration GPU
#SBATCH --mem-per-cpu=10000M            # Mémoire par CPU

# Charger les modules nécessaires
module load python cuda

# Charger l'environnement virtuel
source ENV/bin/activate

# Commandes à exécuter
echo "Début du job"
sleep 15
python additions_sérieuses.py --a 1 --b 2
echo "Fin du job"