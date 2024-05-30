# Calculateur d'intérêts financiers

Ce projet consiste en un calculateur d'intérêts financiers en Python. Il permet de calculer les intérêts simples et composés sur un capital initial donné sur une période définie.

## Fonctionnalités

- Calcul des intérêts simples
- Calcul des intérêts composés
- Interface utilisateur simple avec Tkinter

## Comment utiliser

1. Assurez-vous d'avoir Python installé sur votre machine.
2. Clonez ce dépôt sur votre machine locale.
3. Exécutez le fichier `calcul_interets.py` avec Python.
4. Suivez les instructions pour saisir le capital initial, le taux d'intérêt annuel et le nombre d'années.
5. Consultez les résultats affichés.

## Exemple de code

```python
# Exemple d'utilisation du calculateur d'intérêts financiers
capital_initial = 1000  # Capital initial en euros
taux_interet_annuel = 0.05  # Taux d'intérêt annuel (5%)
nombre_annees = 10  # Nombre d'années

# Calcul des intérêts simples
interets_simples, montant_total_simples = calcul_interets_simples(capital_initial, taux_interet_annuel, nombre_annees)
print(f"Intérêts Simples: {interets_simples:.2f}€, Montant Total: {montant_total_simples:.2f}€")

# Calcul des intérêts composés
interets_composes, montant_total_composes = calcul_interets_composes(capital_initial, taux_interet_annuel, nombre_annees)
print(f"Intérêts Composés: {interets_composes:.2f}€, Montant Final: {montant_total_composes:.2f}€")

©2024 Mulot Steven. Tout droit réservé.
