import os
import pandas as pd

def save_data(X, y, output_dir, prefix, classe):
    os.makedirs(output_dir, exist_ok=True)


    if classe==None:
        # Sauvegarder X
        X_df = pd.DataFrame(X)
        X_path = os.path.join(output_dir, f"{prefix}_X.csv")
        X_df.to_csv(X_path, index=False)
    
        # Sauvegarder y
        y_df = pd.DataFrame(y, columns=["target"])
        y_path = os.path.join(output_dir, f"{prefix}_y.csv")
        y_df.to_csv(y_path, index=False)
    
        print(f"Données sauvegardées : {X_path}, {y_path}")

    else:
        # Sauvegarder X
        X_df = pd.DataFrame(X)
        X_path = os.path.join(output_dir, f"{prefix}_X_{classe}.csv")
        X_df.to_csv(X_path, index=False)
    
        # Sauvegarder y
        y_df = pd.DataFrame(y, columns=["target"])
        y_path = os.path.join(output_dir, f"{prefix}_y_{classe}.csv")
        y_df.to_csv(y_path, index=False)
    
        print(f"Données sauvegardées : {X_path}, {y_path}")