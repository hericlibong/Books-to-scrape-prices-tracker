import csv
import os

def save_to_csv(data_list, filename):
    """Sauvegarde une liste de dictionnaires dans un fichier CSV.

    Args:
        data_list (list): Liste de dictionnaires contenant les données à sauvegarder.
        filename (str): Chemin du fichier CSV où sauvegarder les données.
    """
    if not data_list:
        print("Aucune donnée à sauvegarder.")
        return

    # Détermine les noms des champs à partir du premier élément de la liste
    with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data_list[0].keys())
        writer.writeheader()
        for data in data_list:
            writer.writerow(data)

# def save_to_csv_by_category(data_list, category):
#     filename = f"{category}.csv"
#     with open(filename, mode='a', newline='', encoding='utf-8') as csv_category:
#         writer = csv.DictWriter(csv_category, fieldnames=data_list[0].keys())
#         if csv_category.tell() == 0:
#             writer.writeheader()
#             for data in data_list:  
#                 writer.writerow(data)
            

def save_to_csv_by_category(data_list, category, directory='categories_data'):
    """Sauvegarde une liste de dictionnaires dans un fichier CSV par catégorie.

    Crée un fichier CSV pour chaque catégorie et ajoute les données. Si le fichier
    n'existe pas, il est créé et l'en-tête est ajouté. Si le fichier existe déjà,
    les données sont ajoutées sans répéter l'en-tête.

    Args:
        data_list (list): Liste de dictionnaires contenant les données à sauvegarder.
        category (str): Nom de la catégorie pour nommer le fichier CSV.
        directory (str, optional): Dossier de destination des fichiers CSV. Par défaut à 'categories_data'.
    """
    # Assure-toi que le dossier existe, sinon crée-le
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Construit le chemin complet du fichier
    filename = os.path.join(directory, f"{category}.csv")
    
    with open(filename, mode='a', newline='', encoding='utf-8') as csv_category:
        writer = csv.DictWriter(csv_category, fieldnames=data_list[0].keys())
        if csv_category.tell() == 0:  # Écrit l'en-tête si le fichier est nouveau
            writer.writeheader()
        for data in data_list:  
            writer.writerow(data)
