
def separation_donnees(house_df):
    # Supposons que 'Price' est la colonne cible et les autres colonnes sont des caractéristiques
    X = house_df.drop('Price', axis=1).values  # Variables caractéristiques (features)
    y = house_df['Price'].values  # Variable à prédire (target)

    # Ensemble d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test