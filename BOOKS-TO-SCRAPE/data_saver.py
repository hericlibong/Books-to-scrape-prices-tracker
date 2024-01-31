import csv


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
    #fieldnames = data_list[0].keys()

    with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data_list[0].keys())
        writer.writeheader()
        for data in data_list:
            writer.writerow(data)