import kagglehub  # type: ignore
import pandas as pd  # type: ignore
from sklearn.model_selection import train_test_split  # type: ignore
from sklearn.ensemble import RandomForestClassifier  # type: ignore

# Télécharger le dataset
path = kagglehub.dataset_download("zafarali27/house-price-prediction-dataset")

# Construire le chemin vers le fichier CSV
csv_path = f"{path}/House Price Prediction Dataset.csv"

# Lire le fichier CSV avec pandas
house_df = pd.read_csv(csv_path)

# Afficher les premières lignes
print(house_df.head())

# Vérifier les colonnes et identifier la variable cible
print(house_df.columns)

# Supposons que 'Price' est la colonne cible et les autres colonnes sont des caractéristiques
X = house_df.drop('Price', axis=1).values  # Variables caractéristiques (features)
y = house_df['Price'].values  # Variable à prédire (target)

# Ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Classification des données en catégories RandomForestClassifier
clf = RandomForestClassifier(
     n_estimators=100,
     criterion='gini',
     max_depth=None,
     min_samples_split=2,
     min_samples_leaf=1,
     min_weight_fraction_leaf=0.0,
     max_features='sqrt',
     max_leaf_nodes=None,
     min_impurity_decrease=0.0,
     bootstrap=True,
     oob_score=False,
     n_jobs=None,
     random_state=None,
     verbose=0,
     warm_start=False,
     class_weight=None,
     ccp_alpha=0.0,
     max_samples=None,)



