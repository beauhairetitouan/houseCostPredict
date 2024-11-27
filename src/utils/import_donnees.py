import kagglehub
import pandas as pd

def load_data():
    # Télécharger la dernière version du dataset
    path = kagglehub.dataset_download("sukhmandeepsinghbrar/housing-price-dataset")
    print(f"Données téléchargées : {path}")

    # Construire le chemin vers le fichier CSV
    csv_path = f"{path}/Housing.csv"

    # Lire le fichier CSV avec pandas
    house_df = pd.read_csv(csv_path)

    return house_df
