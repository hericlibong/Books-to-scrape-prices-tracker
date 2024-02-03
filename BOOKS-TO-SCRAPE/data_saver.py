import csv
import os
import re

# def clean_filename(filename):
#     """Supprime les caractères invalides du nom du fichier sous windows"""
#     invalids_charts = ['\\', '/', '*', '?', ':', '"', '<', '>', '|']
#     for char in invalids_charts:
#         filename = filename.replace(char, '')
    
#     filename = filename.replace(' ', '_')
#     return filename


def clean_filename(name):
    """Nettoie le nom pour le rendre valide comme nom de fichier ou dossier sous Windows."""
    invalid_chars = '[\\/*?:"<>|]'  # Caractères invalides à supprimer
    name = re.sub(invalid_chars, '', name)
    name = re.sub(r'\s+', '_', name)  # Remplace les espaces par des underscores
    return name

            

def save_to_csv_by_category(data_list, category, directory='categories_data'):  
    category_cleaned = clean_filename(category)
    
    # Crée le dossier des csv si celui-ci n'existe pas
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    
    # Construit le chemin complet du fichier
    
    filename = os.path.join(directory, f"{category_cleaned}.csv")
    
    with open(filename, mode='w', newline='', encoding='utf-8') as csv_category:
        writer = csv.DictWriter(csv_category, fieldnames=data_list[0].keys())
        if csv_category.tell() == 0:  # Écrit l'en-tête si le fichier est nouveau
            writer.writeheader()
        for data in data_list:  
            writer.writerow(data)
       

def save_image_file(image_file, save_path):
    """Sauvegarde les données binaires de l'image à l'emplacement spécifié"""
    
    #save_path = clean_filename(save_path)  # Nettoie le chemin du fichier
    if image_file:
        os.makedirs(os.path.dirname(save_path), exist_ok=True) #Créé le dossier si jamais celui-ci n'existe pas
        with open(save_path, 'wb') as file:
            file.write(image_file)
    else:
        print("Aucun fichier image n'est à sauvegarder")
