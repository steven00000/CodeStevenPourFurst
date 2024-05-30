import tkinter as tk
from tkinter import messagebox

def calcul_interets_simples(capital_initial, taux_interet_annuel, nombre_annees):
    interets = capital_initial * taux_interet_annuel * nombre_annees
    montant_total = capital_initial + interets
    return interets, montant_total

def calcul_interets_composes(capital_initial, taux_interet_annuel, nombre_annees):
    montant_final = capital_initial * (1 + taux_interet_annuel) ** nombre_annees
    interets = montant_final - capital_initial
    return interets, montant_final

def calculer_interets():
    try:
        capital_initial = float(centry.get())
        taux_interet_annuel = float(tentry.get()) / 100
        nombre_annees = int(nentry.get())

        interets_simples, montant_total_simples = calcul_interets_simples(capital_initial, taux_interet_annuel, nombre_annees)
        interets_composes, montant_total_composes = calcul_interets_composes(capital_initial, taux_interet_annuel, nombre_annees)

        result_text = f"Intérêts Simples: {interets_simples:.2f}€, Montant Total (Simples): {montant_total_simples:.2f}€\n"
        result_text += f"Intérêts Composés: {interets_composes:.2f}€, Montant Final (Composés): {montant_total_composes:.2f}€"

        messagebox.showinfo("Résultats", result_text)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides pour le capital initial, le taux d'intérêt annuel et le nombre d'années.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calcul des Intérêts Financiers")

# Création des widgets
clabel = tk.Label(root, text="Capital initial en euros:")
centry = tk.Entry(root)
tlabel = tk.Label(root, text="Taux d'intérêt annuel (%):")
tentry = tk.Entry(root)
nlabel = tk.Label(root, text="Nombre d'années:")
nentry = tk.Entry(root)
calculate_button = tk.Button(root, text="Calculer", command=calculer_interets)

# Placement des widgets dans la fenêtre
clabel.grid(row=0, column=0, padx=5, pady=5)
centry.grid(row=0, column=1, padx=5, pady=5)
tlabel.grid(row=1, column=0, padx=5, pady=5)
tentry.grid(row=1, column=1, padx=5, pady=5)
nlabel.grid(row=2, column=0, padx=5, pady=5)
nentry.grid(row=2, column=1, padx=5, pady=5)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Lancement de la boucle principale
root.mainloop()
