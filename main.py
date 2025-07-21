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
