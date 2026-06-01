import cv2
from src import pipeline, ocr, detection

img = cv2.imread('test_ab_123_cd.png')
res = pipeline.traiter(img)

print("--- RÉSULTATS DU PIPELINE ---")
print(f"Plaque lue : '{res['plaque']}'")
print(f"Verdict : {res['verdict']}")
print(f"OCR OK : {res['ocr_ok']}")
print(f"Autorisé : {res['autorise']}")

if res['rect']:
    roi = detection.extraire_roi(img, res['rect'])
    plaque_brute = ocr._tesseract_raw(roi) if hasattr(ocr, '_tesseract_raw') else "N/A"
    print(f"\n--- DEBUG TESSERACT ---")
    print(f"Texte brut Tesseract : '{plaque_brute}'")
