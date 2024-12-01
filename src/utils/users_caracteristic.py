

def users_caracteristics():

    date = input("Entrez la date de construction de la maison (AAAAMMJJ) : ")

    bedrooms = input("Entrez le nombre de chambres : ")

    bathrooms = input("Entrez le nombre de salles de bain : ")

    living_area = input("Entrez la superficie de la maison (en pieds carrés) : ")

    lot_area = input("Entrez la superficie du terrain (en pieds carrés) : ")

    floors = input("Entrez le nombre d'étages : ")

    waterfront = input("La maison est-elle en bord de mer ? (0 : non, 1 : oui) : ")

    view = input("Entrez la qualité de la vue (0 : null, 1 : bien, 2 : très bien, 3 : excellent, 4 : incroyable) : ")

    condition = input("Entrez l'état de la maison (1 à 5) : ")

    grade = input("Entrez la notation globale (1 à 13) : ")

    living_area_above_ground = input("Entrez la superficie habitable hors sol (en pieds carrés) : ")

    basement_area = input("Entrez la superficie du sous-sol (en pieds carrés) : ")

    year_built = input("Entrez l'année de construction : ")

    year_renovated = input("Entrez l'année de rénovation : (0 si jamais) ")

    zipcode = input("Entrez le code postal : ")

    latitude = input("Entrez la latitude : ")

    longitude = input("Entrez la longitude : ")

    living_area15 = input("Entrez la moyenne de la superficie habitable (en pieds carrés) des 15 maisons les plus proches : ")

    lot_area15 = input("Entrez la moyenne de la superficie du terrain (en pieds carrés) des 15 maisons les plus proches : ")



    return date, bedrooms, bathrooms, living_area, lot_area, floors, waterfront, view, condition, grade, living_area_above_ground, basement_area, year_built, year_renovated, zipcode, latitude, longitude, living_area15, lot_area15