import sys
import os

# Ajouter le dossier du projet au chemin Python pour importer src
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src import database

# Initialiser la base de données au cas où
database.init_db()

# Liste des plaques à ajouter
plaques = [
    ("AB-123-CD", "Jean Dupont", "Voiture"),
    ("XX-999-YY", "Entreprise Logistique", "Camion"),
    ("AA-000-BB", "Vehicule Service", "Fourgonnette"),
    ("75-ABC-75", "Marie Martin", "Voiture"),
]

print("Ajout des plaques dans la base de données...")
for plaque, proprio, type_v in plaques:
    succes = database.ajouter_plaque(plaque, proprio, type_v)
    if succes:
        print(f"[OK] Plaque ajoutee : {plaque} ({proprio} - {type_v})")
    else:
        print(f"[INFO] La plaque {plaque} est deja dans la base.")
        
print("\nOpération terminée.")
