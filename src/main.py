from src.utils.import_donnees import load_data
from src.utils.encodage_donnees import preprocess_data
from src.models.classification_donnees import classify
from src.models.regression_donnees import regress
from src.utils.users_caracteristic import users_caracteristics

def main():
    # 1. Chargement des données
    house_df = load_data()

    # 2. Prétraitement des données
    house_df, label_encoders = preprocess_data(house_df)

    # 3. Classification
    train_score_class, test_score_class, clf= classify(house_df)
    print(f"Classification - Score entraînement : {train_score_class}")
    print(f"Classification - Score test : {test_score_class}")

    # 4. Régression
    train_score_reg, test_score_reg, cv_score_mean, regressor= regress(house_df)
    print(f"Régression - Score entraînement : {train_score_reg}")
    print(f"Régression - Score test : {test_score_reg}")
    print(f"Régression - Score moyen validation croisée : {cv_score_mean}")

    # 5. Caractéristiques de la maison de l'utilisateur
    users_house = users_caracteristics()

    # 6. Prédiction du prix de la maison de l'utilisateur
    prediction = clf.predict([users_house])
    prediction_price = regressor.predict([users_house])

    print(f"La maison de l'utilisateur est estimée à {prediction[0]} dollars")
    


if __name__ == "__main__":
    main()