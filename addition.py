import torch

"""
Ce script utilise PyTorch pour effectuer une addition simple entre deux tenseurs sur un appareil compatible (GPU ou CPU).

Fonctionnalités principales :
1. Vérifie si CUDA (GPU) est disponible et sélectionne l'appareil approprié (GPU ou CPU).
2. Définit deux nombres sous forme de tenseurs PyTorch sur l'appareil sélectionné.
3. Effectue l'addition des deux tenseurs.
4. Affiche le résultat de l'addition ainsi que l'appareil utilisé.

Ce script est utile pour démontrer l'utilisation de PyTorch avec des opérations simples sur des appareils compatibles.
"""


# Vérifiez si CUDA est disponible
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Définir deux nombres en tant que tenseurs PyTorch
a = torch.tensor([3.0], device=device)
b = torch.tensor([5.0], device=device)

# Additionner les deux tenseurs
result = a + b

# Afficher le résultat
print(f"Résultat de l'addition sur {device}: {result.item()}")