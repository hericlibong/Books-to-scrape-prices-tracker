from data_extraction import*
from data_saver import*
from urllib.parse import urljoin
import os




def process_book(book_url):
    """
    Traite un livre individuel et extrait les données pertinentes.
    
    Args:
        book_url (str): URL de la page du livre à traiter.
        category_name (str): Nom de la catégorie du livre pour le sauvegarde d'images.
        
    Returns:
        dict: Dictionnaire contenant les données extraites du livre.
    """
    
    book_soup = get_soup(book_url) #Obtient le contenu HTML de la page du livre et le convertit en objet BeautifulSoup
    
    # Extrait l'URL de l'image du livre et télécharge les données binaires de l'image
    image_url = get_image_url(book_soup)
    image_file = get_image_file(image_url)
    if image_file:
        save_image_file(image_file, get_category(book_soup), get_universal_product_code(book_soup))

    #retourne un dictionnaire avec les données du livre
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
    """
    Traite tous les livres d'une catégorie, incluant la gestion de la pagination.
    
    Args:
        category_url (str): URL de la catégorie à traiter.
    """
    data_list = [] # Initialise une liste pour stocker les données des livres
    
    while True: # Traore chaque page de la catégorie
        soup = get_soup(category_url)
        book_links = soup.select('h3 a')
        for book in book_links: # Itère sur chaque livre trouvé
            book_url = urljoin(category_url, book['href'])
            data = process_book(book_url) # Passe la fonction process_book pour extraire les données d'un livre
            print(data) # Affiche les données du livre (pour le débogage ou le suivie)
            data_list.append(data)
        
        if data_list: # Sauvegarde les données dans un fichier CSV par catégorie
            save_to_csv_by_category(data_list, data_list[0]['category'])
           

        # Gestion de la pagination
        next_button = soup.find(class_='next')
        if next_button:
            next_page_partial = next_button.find('a')['href'] 
            category_url = urljoin(category_url, next_page_partial) # Prépare de la page suivante
        else:
            break # Sort de la boucle si aucune page suivante n'est trouvée
        

url = 'https://books.toscrape.com/'  #URL de base du site à scraper

def main():
    """
    Point d'entrée principal pour le script de scraping.
    Récupère les liens de toutes les catégories et les traite une par une.
    """
    categories = get_category_links(url)
    for cat_url in categories:
        process_category(cat_url)


if __name__=="__main__":
    main() # Exécute la fonction main si le script est exécuté directement

