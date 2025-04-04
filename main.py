#Importation des bibliothèques nécessaires
import pandas as pd  # Manipulation de données
import numpy as np  # Calculs numériques
import matplotlib.pyplot as plt  # Tracé de graphiques
import seaborn as sns  # Visualisation avancée
import scipy as sp  # Outils statistiques

#  1. Chargement et exploration des données 

# Chargement du dataset à partir du fichier CSV
df = pd.read_csv("/data/analyse_netflix/netflix_titles.csv")

#  Afficher les noms des colonnes
print(df.columns)

# Vérifier le nombre de lignes et de colonnes
print(f"The Number of Rows are {df.shape[0]}, and columns are {df.shape[1]}.")

# Vérifier les types de données de chaque colonne
print(df.info())

# Vérifier les valeurs manquantes
print(df.isnull().sum())

# Vérifier les doublons 
print(f"Nombre de doublons : {df.duplicated().sum()}")

# Voir les premières lignes
print(df.head())  

# Résumé statistique des colonnes numériques
print(df.describe()) 

print(df["type"].value_counts())  # Films vs Séries
