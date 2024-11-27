from src.utils.import_donnees import load_data
from src.utils.encodage_donnees import preprocess_data
from src.models.classification_donnees import classify
from src.models.regression_donnees import regress

def main():
    # 1. Chargement des données
    house_df = load_data()

    # 2. Prétraitement des données
    house_df, label_encoders = preprocess_data(house_df)

    # 3. Classification
    train_score_class, test_score_class = classify(house_df)
    print(f"Classification - Score entraînement : {train_score_class}")
    print(f"Classification - Score test : {test_score_class}")

    # 4. Régression
    train_score_reg, test_score_reg, cv_score_mean = regress(house_df)
    print(f"Régression - Score entraînement : {train_score_reg}")
    print(f"Régression - Score test : {test_score_reg}")
    print(f"Régression - Score moyen validation croisée : {cv_score_mean}")

if __name__ == "__main__":
    main()