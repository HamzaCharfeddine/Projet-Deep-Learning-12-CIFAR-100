"""
Data augmentation

Signature imposée :
get_augmentation_transforms(config: dict) -> objet/transform callable (ou None)
"""

def get_augmentation_transforms(config: dict):
    """Retourne les transformations d'augmentation. À implémenter."""
    raise NotImplementedError("get_augmentation_transforms doit être implémentée par l'étudiant·e.")