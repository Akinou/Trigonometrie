import math

# Demander à l'utilisateur de saisir un angle en degrés
deg = float(input("Entrez un angle en degrés: "))

# Convertir l'angle en radians
rad = math.radians(deg)

# Calculer les fonctions trigonométriques
sin = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

# Calculer les fonctions trigonométriques inverses
asin = math.asin(sin)
acos = math.acos(cos)
atan = math.atan(tan)

# Convertir les angles en degrés
asin_deg = math.degrees(asin)
acos_deg = math.degrees(acos)
atan_deg = math.degrees(atan)

# Afficher les résultats
print(f"Sin({deg}) = {sin:.3f}")
print(f"Cos({deg}) = {cos:.3f}")
print(f"Tan({deg}) = {tan:.3f}")
print(f"Asin({sin:.3f}) = {asin_deg:.3f}")
print(f"Acos({cos:.3f}) = {acos_deg:.3f}")
print(f"Atan({tan:.3f}) = {atan_deg:.3f}")
