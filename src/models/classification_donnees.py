from src.utils.extraction_csv import save_data
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def classify(house_df):
    # Préparation des données
    X = house_df.drop(['price', 'price_category'], axis=1).values
    y_class = house_df['price_category'].values

    # Séparer les données
    X_train, X_test, y_train, y_test = train_test_split(X, y_class, test_size=0.2, random_state=42)

    # Sauvegarder les données
    save_data(X_train, y_train, "outputs", "classification_train", None)
    save_data(X_test, y_test, "outputs", "classification_test", None)

    # Modèle et entraînement
    clf = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        min_samples_split=5,
        class_weight='balanced',
        random_state=42
    )
    clf.fit(X_train, y_train)

    return clf.score(X_train, y_train), clf.score(X_test, y_test), clf


