import torch
import argparse

"""
Ce script utilise PyTorch pour effectuer une très longue addition entre deux tenseurs sur un appareil compatible (GPU ou CPU).

Fonctionnalités principales :
1. Vérifie si CUDA (GPU) est disponible et sélectionne l'appareil approprié (GPU ou CPU).
2. Définit deux nombres sous forme de tenseurs PyTorch sur l'appareil sélectionné.
3. Effectue l'addition des deux tenseurs.
4. Affiche le résultat de l'addition ainsi que l'appareil utilisé.

Ce script est utile pour démontrer l'utilisation de PyTorch avec des opérations simples sur des appareils compatibles.
"""

# Configuration des arguments
parser = argparse.ArgumentParser(description="Effectuer une addition sérieuse avec PyTorch.")
parser.add_argument("--a", type=float, required=True, help="Le premier nombre à additionner.")
parser.add_argument("--b", type=float, required=True, help="Le deuxième nombre à additionner.")
args = parser.parse_args()

# Vérifiez si CUDA est disponible
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Appareil utilisé pour le calcul : {device}")

# Définir deux nombres en tant que tenseurs PyTorch
a = torch.tensor([args.a], device=device)
b = torch.tensor([args.b], device=device)

# Sérieusement Additionner
result = a

for i in range(1000000):
    result = result + b

# Afficher le résultat
print(f"Résultat de l'addition sur {device}: {result.item()}")