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
