"""
Chargement des données.

Signature imposée :
get_dataloaders(config: dict) -> (train_loader, val_loader, test_loader, meta: dict)

Le dictionnaire meta doit contenir au minimum :
- "num_classes": int
- "input_shape": tuple (ex: (3, 32, 32) pour des images)
"""

def get_dataloaders(config: dict):
    """
    Crée et retourne les DataLoaders d'entraînement/validation/test et des métadonnées.
    À implémenter.
    """
    raise NotImplementedError("get_dataloaders doit être implémentée par l'étudiant·e.")