
def encodage_donnees(house_df):
    categorical_cols = house_df.select_dtypes(include=['object']).columns

    # Encoder les colonnes catégoriques avec LabelEncoder
    label_encoders = {}
    for col in categorical_cols:
        le = LabelEncoder()
        house_df[col] = le.fit_transform(house_df[col])
        label_encoders[col] = le  
    
    return house_df, label_encoders
