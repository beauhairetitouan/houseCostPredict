import tkinter as tk
from tkinter import messagebox
from src.models.classification_donnees import classify
from src.models.regression_donnees import regress
from src.utils.import_donnees import load_data
from src.utils.encodage_donnees import preprocess_data


class HousePriceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Estimation du prix de la maison")

        # Préparer les modèles et afficher les scores
        self.init_models_and_scores()

        # Dictionnaire pour stocker les entrées utilisateur
        self.user_inputs = {}

        # Labels et champs d'entrée
        self.create_input_field("date", "Date de construction (AAAAMMJJ) :")
        self.create_input_field("bedrooms", "Nombre de chambres :")
        self.create_input_field("bathrooms", "Nombre de salles de bain :")
        self.create_input_field("living_area", "Superficie habitable (pieds²) :")
        self.create_input_field("lot_area", "Superficie du terrain (pieds²) :")
        self.create_input_field("floors", "Nombre d'étages :")
        self.create_input_field("waterfront", "Bord de mer (0 : non, 1 : oui) :")
        self.create_input_field("view", "Qualité de la vue (0 à 4) :")
        self.create_input_field("condition", "État de la maison (1 à 5) :")
        self.create_input_field("grade", "Note globale (1 à 13) :")
        self.create_input_field("living_area_above_ground", "Superficie hors sol (pieds²) :")
        self.create_input_field("basement_area", "Superficie du sous-sol (pieds²) :")
        self.create_input_field("year_built", "Année de construction :")
        self.create_input_field("year_renovated", "Année de rénovation (0 si jamais) :")
        self.create_input_field("zipcode", "Code postal :")
        self.create_input_field("latitude", "Latitude :")
        self.create_input_field("longitude", "Longitude :")
        self.create_input_field("living_area15", "Superficie habitable moyenne (15 proches) (pieds²) :")
        self.create_input_field("lot_area15", "Superficie terrain moyenne (15 proches) (pieds²) :")

        # Bouton pour prédire le prix
        predict_button = tk.Button(root, text="Estimer le prix", command=self.predict_price)
        predict_button.grid(row=len(self.user_inputs)+1, column=1, pady=10)

        # Résultat de la prédiction
        self.result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.result_label.grid(row=len(self.user_inputs) + 1, column=0, columnspan=2)

    def init_models_and_scores(self):
        """Initialise les modèles et affiche les scores."""
        try:
            # Chargement et prétraitement des données
            house_df = load_data()
            house_df, _ = preprocess_data(house_df)

            # Classification
            self.train_score_class, self.test_score_class, self.clf = classify(house_df)

            # Régression
            self.train_score_reg, self.test_score_reg, self.cv_score_mean, self.regressor = regress(house_df)

            # Afficher les scores
            scores_text = (
                f"Scores Classification :\n"
                f"  - Entraînement : {self.train_score_class:.6f}\n"
                f"  - Test : {self.test_score_class:.6f}\n\n"
                f"Scores Régression :\n"
                f"  - Entraînement : {self.train_score_reg:.6f}\n"
                f"  - Test : {self.test_score_reg:.6f}\n"
                f"  - Validation croisée : {self.cv_score_mean:.6f}\n"
            )
            scores_label = tk.Label(self.root, text=scores_text, font=("Arial", 10), justify="left")
            scores_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite lors de l'initialisation : {e}")
            self.clf = None
            self.regressor = None

    def create_input_field(self, field_name, field_label):
        row = len(self.user_inputs) + 1  # Décalage des scores
        label = tk.Label(self.root, text=field_label)
        label.grid(row=row, column=0, sticky="w", padx=10, pady=5)
        entry = tk.Entry(self.root)
        entry.grid(row=row, column=1, padx=10, pady=5)
        self.user_inputs[field_name] = entry

    def predict_price(self):
        try:
            # Vérifier que les modèles sont prêts
            if self.clf is None or self.regressor is None:
                raise ValueError("Les modèles n'ont pas été correctement initialisés.")

            # Collecte des données utilisateur
            user_data = [float(self.user_inputs[field].get()) for field in self.user_inputs]

            # Prédiction du prix
            classification = self.clf.predict([user_data])[0]
            prediction_price = self.regressor.predict([user_data])[0]

            self.result_label.config(
                text=(
                    f"Classification : {classification}\n"
                    f"Estimation : {prediction_price:,.2f} dollars"
                )
            )
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")


if __name__ == "__main__":
    
    root = tk.Tk()
    print(f"Ouverture de la fenêtre... Veuillez patienter.")
    app = HousePriceApp(root)
    print(f"Une fenêtre s'est ouverte pour estimer le prix de votre maison.")
    root.mainloop()
    
    
    
