

def import_donnees():

    path = kagglehub.dataset_download("zafarali27/house-price-prediction-dataset")

    csv_path = f"{path}/House Price Prediction Dataset.csv"

    house_df = pd.read_csv(csv_path)

    return house_df