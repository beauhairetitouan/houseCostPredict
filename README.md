# House Cost Predict (HCP)
## BEAUHAIRE Titouan / ROVIRA Adrien

### Introduction

[Sujet du projet](docs/Sujet_Projet_IA_BEAUHAIRE_ROVIRA.pdf)

[Données du projet](https://www.kaggle.com/datasets/sukhmandeepsinghbrar/housing-price-dataset)


### Structure du projet

![Python](https://img.shields.io/badge/Language-Python-green.svg)
[![Kaggle Dataset](https://img.shields.io/badge/Kaggle-Dataset-blue.svg)](https://www.kaggle.com/datasets/zafarali27/house-price-prediction-dataset)
![Pandas](https://img.shields.io/badge/Library-Pandas-purple.svg)
![Scikit-learn](https://img.shields.io/badge/Library-Scikit--learn-red.svg)
[![KaggleHub](https://img.shields.io/badge/KaggleHub-Project-yellow.svg)](https://www.kaggle.com/kagglehub/ton-projet)


- **`housecostpredict/`** : Le répertoire racine du projet
    - **`.venv/`** : Le répertoire de configuration de l'environnement virtuel
    - **`data/`** : Le répertoire qui sauvegarde les états du jeu de données
        - **`Housing.csv`** : Fichier du jeu de données initial
    - **`docs/`** : Le répertoire qui sauvegarde toute la documentation du projet
        - **`Sujet_Projet_IA_BEAUHAIRE_ROVIRA`** : Le fichier qui décrit et introduit le sujet
    - **`lib/`** : Le répertoire qui sauvegarde les configurations d'installation des librairies
        - **`requirements.txt`** : Le fichier qui liste les librairies à installer avec leur version
    - **`outputs/`** : Répertoire sauvegardant les données d'entrainements et de tests
    - **`src/`** : Le répertoire principal où le code source du projet est contenu
        - **`models/`** : Répertoire regroupant les différents models d'apprentissage
        - **`utils/`** : Répertoire qui contient les outils nécessaires aux imports, encodage des données, entrées de l'utilisateur et l'extraction des fichiers csv
        - **`main`** : Fichier principal (controller) qui gère les étapes du programme une par une 
    - **`.gitignore`** : Le fichier qui liste les répertoires et fichiers à ignorer dans git
    - **`README.md`** : Le fichier qui introduit le projet




### Installation du projet


- Clonez le projet

    ```shell
    git clone https://github.com/beauhairetitouan/houseCostPredict.git
    ```

- Déplacez vous vers le dossier housecostpredict/

    ```shell
    cd housecostpredict/
    ```

- Téléchargez et installez Python avec la version minimale 3.11.4

- Créez l'environnement virtuel

    ```shell
    python -m venv .venv
    ```

- Activez l'environnement virtuel

    - Sur Windows

        ```shell
        .\.venv\Scripts\activate
        ```

    - Sur macOS/Linux

        ```shell
        source .venv/bin/activate
        ```


- Lancez la commande suivante pour installer toutes les librairies nécessaires:

    ```shell
    pip install -r lib/requirements.txt
    ```

### Démarrage du projet

- Lancez l'application

    ```shell
    python -m src.main
    ```
    Une fenêtre va s'ouvrir...

- Désactivez l'environnement virtuel

    ```shell
    deactivate
    ```

