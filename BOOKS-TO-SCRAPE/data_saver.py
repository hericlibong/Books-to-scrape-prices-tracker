import csv
import os
import re

def clean_filename(name):
    """
    Nettoie le nom pour le rendre valide comme nom de fichier ou dossier sous Windows.
    
    Args:
        name (str): Le nom du fichier ou dossier à nettoyer.
        
    Returns:
        str: Le nom nettoyé, sans caractères invalides et avec des espaces remplacés par des underscores.
    """
    invalid_chars = '[\\/*?:"<>|]'  # Caractères invalides à supprimer.
    name = re.sub(invalid_chars, '', name)  # Supprime les caractères invalides.
    name = re.sub(r'\s+', '_', name)  # Remplace les espaces par des underscores.
    return name





def save_to_csv_by_category(data_list, category, directory='categories_data'):
    """
    Sauvegarde les données par catégorie dans un fichier CSV dans le répertoire spécifié.
    
    Args:
        data_list (list): Liste des dictionnaires contenant les données à sauvegarder.
        category (str): Nom de la catégorie pour nommer le fichier.
        directory (str): Chemin du répertoire où sauvegarder le fichier CSV. Par défaut, 'categories_data'.
    """
    category_cleaned = clean_filename(category)  # Nettoie le nom de la catégorie pour le fichier.
    
    if not os.path.exists(directory):
        os.makedirs(directory)  # Crée le dossier si non existant.
    
    filename = os.path.join(directory, f"{category_cleaned}.csv")  # Construit le chemin du fichier.
    
    with open(filename, mode='w', newline='', encoding='utf-8') as csv_category:
        writer = csv.DictWriter(csv_category, fieldnames=data_list[0].keys())
        if csv_category.tell() == 0:  # Écrit l'en-tête si le fichier est vide.
            writer.writeheader()
        for data in data_list:
            writer.writerow(data)  # Écrit les données dans le fichier.





def save_image_file(image_file, save_path):
    """
    Sauvegarde les données binaires de l'image à l'emplacement spécifié.
    
    Args:
        image_file (bytes): Données binaires de l'image à sauvegarder.
        save_path (str): Chemin complet où sauvegarder l'image.
    """
    if image_file:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Crée le dossier si nécessaire.
        with open(save_path, 'wb') as file:
            file.write(image_file)  # Écrit les données de l'image dans le fichier.
    else:
        print("Aucun fichier image n'est à sauvegarder.")  # Gère le cas où aucune image n'est disponible.
