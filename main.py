import tkinter as tk
from tkinter import messagebox
import csv
import os



# Chemin du fichier CSV
FICHIER = "contacts.csv"

# Fonction pour enregistrer un contact
def enregistrer_contact():
    nom = name_var.get()
    telephone = phone_var.get()
    email = email_var.get()
    genre = gender_var.get()

    if not nom or not telephone:
        messagebox.showwarning("Champs vides", "Nom et téléphone sont obligatoires.")
        return

    with open(FICHIER, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([nom, telephone, email, genre])
    
    messagebox.showinfo("Succès", "Contact enregistré avec succès !")
    effacer_champs()

    # Fonction pour afficher les contacts
def afficher_contacts():
    if not os.path.exists(FICHIER):
        messagebox.showinfo("Info", "Aucun contact enregistré.")
        return

    fenetre_contacts = tk.Toplevel(root)
    fenetre_contacts.title("Liste des contacts")


    with open(FICHIER, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            tk.Label(fenetre_contacts, text=" | ".join(row)).grid(row=i, column=0, sticky='w')


# Effacer les champs du formulaire
def effacer_champs():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    gender_var.set("")

# Fenêtre principale
root = tk.Tk()
root.title("Gestionnaire de Contacts")

# Variables
name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
gender_var = tk.StringVar()


# Interface utilisateur
tk.Label(root, text="Nom").grid(row=0, column=0, padx=10, pady=5, sticky='w')
tk.Entry(root, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Téléphone").grid(row=1, column=0, padx=10, pady=5, sticky='w')
tk.Entry(root, textvariable=phone_var).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=5, sticky='w')
tk.Entry(root, textvariable=email_var).grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Genre").grid(row=3, column=0, padx=10, pady=5, sticky='w')
tk.Entry(root, textvariable=gender_var).grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Enregistrer", command=enregistrer_contact).grid(row=4, column=0, pady=10)
tk.Button(root, text="Afficher les contacts", command=afficher_contacts).grid(row=4, column=1, pady=10)

root.mainloop()
