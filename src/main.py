import kagglehub 
import pandas as pd 
from sklearn.model_selection import train_test_split, cross_val_score 
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor 
from sklearn.preprocessing import LabelEncoder 

# Télécharger la dernière version du dataset
path = kagglehub.dataset_download("zafarali27/house-price-prediction-dataset")

# Construire le chemin vers le fichier CSV
csv_path = f"{path}/House Price Prediction Dataset.csv"

# Lire le fichier CSV avec pandas
house_df = pd.read_csv(csv_path)

# Sélectionner les colonnes catégorielles
categorical_cols = house_df.select_dtypes(include=['object']).columns

# Encoder les colonnes catégorielles avec LabelEncoder
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    house_df[col] = le.fit_transform(house_df[col])
    label_encoders[col] = le 

# Vérifier les colonnes après encodage
print("Colonnes après encodage :")
print(house_df.head())

# Afficher les colonnes du dataframe
print(house_df.columns)

print(min(house_df['Price']), max(house_df['Price']))
# 1. Classification : prédiction de la catégorie de prix
# Par exemple, on crée une variable 'Price_Category' en fonction du prix
house_df['Price_Category'] = pd.qcut(house_df['Price'], q=4, labels=[0, 1, 2, 3])

print(house_df['Price_Category'].value_counts())

X = house_df.drop(['Price', 'Price_Category'], axis=1).values 
y_class = house_df['Price_Category'].values  

# Séparer l'ensemble d'entraînement et de test pour la classification
X_train, X_test, y_train_class, y_test_class = train_test_split(X, y_class, test_size=0.2, random_state=42)

# Classification des données avec RandomForestClassifier
clf = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    class_weight='balanced',
    random_state=42
)

# Entraîner le modèle de classification
clf.fit(X_train, y_train_class)


# Évaluer la classification
print("Classification - Score sur l'ensemble d'entraînement :", clf.score(X_train, y_train_class))
print("Classification - Score sur l'ensemble de test :", clf.score(X_test, y_test_class))

# 2. Régression : prédiction du prix exact
y_reg = house_df['Price'].values

# Séparer l'ensemble d'entraînement et de test pour la régression
X_train, X_test, y_train_reg, y_test_reg = train_test_split(X, y_reg, test_size=0.2, random_state=42)

# Régression avec RandomForestRegressor
regressor = RandomForestRegressor(
    n_estimators=200,
    max_depth=20,
    min_samples_split=3,
    random_state=42
)

# Entraîner le modèle de régression
regressor.fit(X_train, y_train_reg)

# Évaluer la régression
print("Régression - Score sur l'ensemble d'entraînement :", regressor.score(X_train, y_train_reg))
print("Régression - Score sur l'ensemble de test :", regressor.score(X_test, y_test_reg))

# Validation croisée pour évaluer la performance du modèle de régression
scores = cross_val_score(regressor, X, y_reg, cv=5)  # 5-fold cross-validation
print(f"Scores de validation croisée : {scores}")
print(f"Score moyen de validation croisée : {scores.mean()}")
