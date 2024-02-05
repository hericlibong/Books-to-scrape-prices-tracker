from data_extraction import*
from data_saver import*
from urllib.parse import urljoin
import os


url = 'https://books.toscrape.com/'


def process_book(book_url, category_name):
    """Traite un livre individuel.Prend l'URL du livre et le nom de la catégorie en paramètres"""
    
    book_soup = get_soup(book_url) #Obtient le contenu HTML de la page du livre et le convertit en objet BeautifulSoup
    
    # Extrait les données de l'image du livre et télécharge les données binaires de l'image
    image_url = get_image_url(book_soup)
    image_file = get_image_file(image_url)

    #Nettoie le titre du livre pour l'utiliser comme nom de fichier avec une limitation 
    #de longueur pour éviter les problèmes avec les systèmes de fichcier
    #Contruit le chemin complet où l'image sera sauvegardée(dossier/sous-dossier)
    MAX_TITLE_LENGTH = 80
    book_title_cleaned = clean_filename(get_title(book_soup))[:MAX_TITLE_LENGTH]
    image_save_path = os.path.join('book_images', category_name, f"{book_title_cleaned}.jpg")

    #si les données de l'image sont disponibles, sauvegarde de l'image dans le chemin spécifié
    if image_file:
        save_image_file(image_file, image_save_path)
    

    #retourne un dictionnaire contenant les données extraites du livre
    return {
            'product_page_url': book_url,
            'universal_product_code': get_universal_product_code(book_soup),
            'title': get_title(book_soup),
            'price_including_tax': get_price_including_tax(book_soup),
            'price_excluding_tax': get_price_excluding_tax(book_soup),
            'number_available': get_number_available(book_soup),
            'product_description': get_product_description(book_soup),
            'category': get_category(book_soup),
            'review_rating': get_star_rating(book_soup),
            'image_url': get_image_url(book_soup)
    }


def process_category(category_url):
    """Fonction pour traiter tous les livres d'une catégorie tenant compte de la pagination"""
    data_list = [] 
    
    #Initialise une liste pour stocker les données de tous les livres d'une catégorie
    #Entame une boucle pour traiter chaque page de la catégorie
    #Obtient le contenu de la page actuelle et extrait les liens vers les livres
    #Itère sur chaque lien de livre trouvé 
    
    while True:
        soup = get_soup(category_url)
        book_links = soup.select('h3 a')
        for book in book_links:
            book_url = urljoin(category_url, book['href'])

            #Construit l'URL complète du livre et appelle 'process_book' pour traiter le livre
            data = process_book(book_url, get_category(get_soup(book_url)))
            print(data)
            data_list.append(data)

        # Si les données sont collectées, elles sont sauvegardées par catégorie dans un fichier csv
        if data_list:
            save_to_csv_by_category(data_list, data_list[0]['category'])
            data_list = [] # Réinitialise la liste pour la prochaine page

        # --Génèration de la pagination---
        next_button = soup.find(class_='next')
        if next_button:
            next_page_partial = next_button.find('a')['href'] # Récupère le lien de la page suivante
            category_url = urljoin(category_url, next_page_partial) # Reconstruction du lien vers la page suivante
        else:
            break # Stop la boucle si la page suivante n'est pas trouvée
        
# Point d'entrée principal
#Définit la fonction principale qui commence par récupérer 
# tous les liens de catégories et les traite un par un.
def main():
    categories = get_category_links(url)
    for cat_url in categories:
        process_category(cat_url)


if __name__=="__main__":
    main()

