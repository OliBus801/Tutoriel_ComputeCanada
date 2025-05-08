#!/bin/bash
#SBATCH --output=logs/resultat_%A_%a.out       # Fichier de sortie pour chaque tâche
#SBATCH --time=00:30:00                        # Temps d'exécution (hh:mm:ss)
#SBATCH --gpus-per-task=0                      # Un GPU par tâche
#SBATCH --mem-per-cpu=10000M                   # Mémoire par CPU
#SBATCH --array=1-50:10                            # Définir un array job avec 10 tâches (index 0 à 9)

# Charger les modules nécessaires
module load python 

# Charger l'environnement virtuel
source ENV/bin/activate

# Commandes à exécuter
echo "Début du job pour la tâche $SLURM_ARRAY_TASK_ID"
sleep 15
python additions_sérieuses.py --a $SLURM_ARRAY_TASK_ID --b $(($SLURM_ARRAY_TASK_ID + 10))
echo "Fin du job pour la tâche $SLURM_ARRAY_TASK_ID"