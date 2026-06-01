import cv2
import numpy as np
import os

# Créer une image de fond (simulant un bout de voiture)
img = np.full((600, 800, 3), 150, dtype=np.uint8)

# Dessiner une calandre / pare-chocs
cv2.rectangle(img, (150, 350), (650, 550), (80, 80, 80), -1)

# --- Plaque d'immatriculation ---
# Dimensions avec un ratio d'environ 4 à 5
px, py, pw, ph = 250, 420, 300, 70
# Fond blanc
cv2.rectangle(img, (px, py), (px+pw, py+ph), (255, 255, 255), -1)
# Bordure noire
cv2.rectangle(img, (px, py), (px+pw, py+ph), (0, 0, 0), 3)

# Ajouter le texte "AB-123-CD"
texte = "AB-123-CD"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.3
thickness = 3

# Calculer la position pour centrer le texte
text_size = cv2.getTextSize(texte, font, font_scale, thickness)[0]
text_x = px + (pw - text_size[0]) // 2
text_y = py + (ph + text_size[1]) // 2

cv2.putText(img, texte, (text_x, text_y), font, font_scale, (0, 0, 0), thickness, cv2.LINE_AA)

# Sauvegarder l'image
chemin = "test_ab_123_cd.png"
cv2.imwrite(chemin, img)
print(f"Image de test générée avec succès : {os.path.abspath(chemin)}")
