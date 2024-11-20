import kagglehub

# Download latest version
path = kagglehub.dataset_download("zafarali27/house-price-prediction-dataset")

print("Path to dataset files:", path)