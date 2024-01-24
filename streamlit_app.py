import random
import json
import streamlit as st


class Recette:
    def __init__(self, nom, ingredients, quantites, saison):
        self.nom = nom
        self.ingredients = ingredients
        self.quantites = quantites
        self.saison = saison

    def afficher_nom(self):
        print("Nom du plat:", self.nom)
        print()

    def afficher_ingredients(self):
        print("Ingrédients:")
        for i in range(len(self.ingredients)):
            print(f"  - {self.ingredients[i]}: {self.quantites[i]}")
        print()
        print("Saison:", self.saison)
        print()


# Fonction pour sauvegarder les recettes dans un fichier JSON
def sauvegarder_recettes():
    with open('recettes.json', 'w') as fichier:
        json.dump([recette.__dict__ for recette in recettes], fichier)


# Fonction pour charger les recettes depuis un fichier JSON
def charger_recettes():
    try:
        with open('recettes.json', 'r') as fichier:
            data = json.load(fichier)
            return [Recette(recette['nom'], recette['ingredients'], recette['quantites'], recette['saison']) for recette
                    in data]
    except FileNotFoundError:
        return []


# Liste pour stocker les recettes
recettes = charger_recettes()


def afficher_recettes():
    if not recettes:
        print("Aucune recette disponible.")
        return

    print("Liste des recettes:")

    for i, recette in enumerate(recettes):
        print(f"{i + 1}. {recette.nom}")

    choix = input("Choisissez le numéro de la recette à préparer : ")

    try:
        index = int(choix) - 1
        if 0 <= index < len(recettes):
            recette_choisie = recettes[index]
            recette_choisie.afficher_nom()
            recette_choisie.afficher_ingredients()
        else:
            print("Numéro de recette invalide.")

    except ValueError:
        print("Veuillez entrer un numéro valide.")


def ajouter_recette():
    nom = input("Nom du plat: ")
    ingredients = input("Ingrédients (séparés par des virgules): ").split(',')
    quantites = input("Quantités correspondantes (séparées par des virgules): ").split(',')
    saison = input("Saison (été/hiver): ").lower()

    recette = Recette(nom, ingredients, quantites, saison)
    recettes.append(recette)
    sauvegarder_recettes()
    print("Recette ajoutée avec succès!")


def supprimer_recette():
    if not recettes:
        print("Aucune recette disponible.")
        return

    print("Liste des recettes:")
    for i, recette in enumerate(recettes):
        print(f"{i + 1}. {recette.nom}")

    choix = input("Choisissez le numéro de la recette à supprimer: ")

    try:
        index = int(choix) - 1
        if 0 <= index < len(recettes):
            del recettes[index]
            sauvegarder_recettes()
            print("Recette supprimée avec succès!")
        else:
            print("Numéro de recette invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")


def modifier_recette():
    if not recettes:
        print("Aucune recette disponible.")
        return

    print("Liste des recettes:")
    for i, recette in enumerate(recettes):
        print(f"{i + 1}. {recette.nom}")

    choix = input("Choisissez le numéro de la recette à modifier: ")

    try:
        index = int(choix) - 1
        if 0 <= index < len(recettes):
            # Modification des détails de la recette
            recette = recettes[index]
            print(f"Modification de la recette '{recette.nom}':")
            recette.nom = input("Nouveau nom du plat: ")
            recette.ingredients = input("Nouveaux ingrédients (séparés par des virgules): ").split(',')
            recette.quantites = input("Nouvelles quantités correspondantes (séparées par des virgules): ").split(',')
            recette.saison = input("Nouvelle saison (été/hiver): ").lower()

            sauvegarder_recettes()
            print("Recette modifiée avec succès!")
        else:
            print("Numéro de recette invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")


def tirer_au_sort():
    if not recettes:
        print("Aucune recette disponible.")
        return

    recette_choisie = random.choice(recettes)
    recette_choisie.afficher_nom()

    print()
    reponse = input("Voulez-vous afficher la liste des ingrédients ? (O/N): ").lower()
    if reponse == 'o':
        print()
        recette_choisie.afficher_nom()
        recette_choisie.afficher_ingredients()


# Menu principal
while True:
    print()
    print("1. Afficher les recettes")
    print("2. Ajouter une recette")
    print("3. Supprimer une recette")
    print("4. Modifier une recette")
    print("5. Tirer une recette au sort")
    print("6. Quitter")

    choix = input("Choisissez une option (1/2/3/4/5/6): ")
    print()

    if choix == '1':
        afficher_recettes()
    elif choix == '2':
        ajouter_recette()
    elif choix == '3':
        supprimer_recette()
    elif choix == '4':
        modifier_recette()
    elif choix == '5':
        tirer_au_sort()
    elif choix == '6':
        print("Au revoir!")
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")
