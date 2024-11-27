from sklearn.preprocessing import LabelEncoder
import pandas as pd

def preprocess_data(house_df):
    # Standardiser les noms de colonnes pour éviter des erreurs de casse
    house_df.columns = house_df.columns.str.lower()

    # Sélectionner les colonnes catégorielles
    categorical_cols = house_df.select_dtypes(include=['object']).columns

    # Encoder les colonnes catégorielles avec LabelEncoder
    label_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        house_df[col] = le.fit_transform(house_df[col])
        label_encoders[col] = le

    # Création de la variable catégorielle 'price_category' en fonction du prix
    house_df['price_category'] = pd.qcut(house_df['price'], q=4, labels=[0, 1, 2, 3])

    return house_df, label_encoders
