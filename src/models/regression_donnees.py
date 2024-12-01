from src.utils.extraction_csv import save_data
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score

def regress(house_df):
   
    # Extraction des caractéristiques et de la cible
    X = house_df.drop(['price', 'price_category'], axis=1).values
    classe = house_df['price_category'].values[0]
    y_reg = house_df['price'].values



    # Séparer l'ensemble d'entraînement et de test
    X_train, X_test, y_train_reg, y_test_reg = train_test_split(X, y_reg, test_size=0.2, random_state=42)

    # Sauvegarder les données 
    save_data(X_train, y_train_reg, "outputs", "regression_train", classe)
    save_data(X_test, y_test_reg, "outputs", "regression_test", classe)

    # Régression avec RandomForestRegressor
    regressor = RandomForestRegressor(
        n_estimators=50,
        max_depth=10,
        min_samples_split=3,
        random_state=42
    )

    # Entraîner le modèle
    regressor.fit(X_train, y_train_reg)

    # Évaluer le modèle
    train_score = regressor.score(X_train, y_train_reg)
    test_score = regressor.score(X_test, y_test_reg)

    # Validation croisée
    scores = cross_val_score(regressor, X, y_reg, cv=5)

    return train_score, test_score, scores.mean(), regressor
