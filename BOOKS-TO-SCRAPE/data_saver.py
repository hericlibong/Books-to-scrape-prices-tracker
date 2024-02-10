import csv
import os
import re



def clean_filename(name):
    """
    Nettoie le nom pour le rendre valide comme nom de fichier ou dossier sous Windows. 
    Nettoie aussi les noms de dossiers des catégories.

    Args:
        name (str): Le nom du fichier ou dossier à nettoyer.
        
    Returns:
        str: Le nom nettoyé, sans caractères invalides et avec des espaces remplacés par des underscores.
    """
    invalid_chars = '[\\/*?:"<>|]'  # Caractères invalides à supprimer.
    name = re.sub(invalid_chars, '', name)  # Supprime les caractères invalides.
    name = re.sub(r'\s+', '_', name)  # Remplace les espaces par des underscores.
    return name



# Sauvegarde des données des livres par catégorie

def save_to_csv_by_category(data_list, category, directory='categories_data'):
    """
    Sauvegarde les données par catégorie dans un fichier CSV dans le répertoire spécifié.
    
    Args:
        data_list (list): Liste des dictionnaires contenant les données à sauvegarder.
        category (str): Nom de la catégorie pour nommer le fichier.
        directory (str): Chemin du répertoire où sauvegarder le fichier CSV. Par défaut, 'categories_data'.
    """
    category_cleaned = clean_filename(category)  # Nettoie le nom de la catégorie pour le fichier.
    
    
    os.makedirs(directory, exist_ok=True)  # Crée le dossier si non existant.
    
    filename = os.path.join(directory, f"{category_cleaned}.csv")  # Construit le chemin du fichier.
    
    with open(filename, mode='w', newline='', encoding='utf-8') as csv_category:
        writer = csv.DictWriter(csv_category, fieldnames=data_list[0].keys())
        if csv_category.tell() == 0:  # Écrit l'en-tête si le fichier est vide.
            writer.writeheader()
        for data in data_list:
            writer.writerow(data)  # Écrit les données dans le fichier.




# Sauvegarde des images
            
def save_image_file(image_file, category, attribut, base_directory='book_images', max_title_length=80):
    """
    Sauvegarde une image téléchargée dans un répertoire spécifié, en utilisant un titre nettoyé et limité en longueur
    pour le nom de fichier, organisé par catégorie.

    Args:
        image_file (bytes): Les données binaires de l'image à sauvegarder.
        attribut (str): l'attribut du livre utilisé pour nommer le fichier image.
        category (str): La catégorie du livre, utilisée pour organiser les images dans des sous-dossiers.
        base_directory (str, optional): Le dossier de base pour sauvegarder les images. Par défaut à 'book_images'.
        max_title_length (int, optional): La longueur maximale du titre pour éviter les erreurs liées à des noms de fichiers trop longs. Par défaut à 80.

    Retourne:
        None. Crée un fichier image dans le système de fichiers, ou affiche un message si aucun fichier image n'est à sauvegarder.
    """
    #title_cleaned = clean_filename(title)[:max_title_length]
    image_save_path = os.path.join(base_directory, clean_filename(category), f"{attribut}.jpg")

    if image_file:
        os.makedirs(os.path.dirname(image_save_path), exist_ok=True)
        with open(image_save_path, 'wb') as file:
            file.write(image_file)
    else:
        print("Aucun fichier image n'est à sauvegarder")


