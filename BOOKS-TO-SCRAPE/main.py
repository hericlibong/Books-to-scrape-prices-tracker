from data_extraction import*
from urllib.parse import urljoin
from data_saver import save_to_csv_by_category, save_image_file, clean_filename
import os

url = 'https://books.toscrape.com/'

def get_category_links(start_url):
    """
    extrait la liste des catégories à partir de l'url du site

    arg:
    url du site
    
    return:
    la liste des catégories exclut la base liste (list)
    """
    soup = get_soup(start_url)
    category_list = []
    list_link = soup.find('ul', class_= 'nav').find_all('li')
    for a in list_link:
        category_list.append(start_url + a.find('a')['href'])
   
    return category_list[1:]


categories = get_category_links(url)

for categorie_url in categories:
    # Réinitialise data_list pour chaque nouvelle catégorie
    data_list = []
    
    while True:
        soup = get_soup(categorie_url)
        book_links = soup.select('h3 a')
        for book in book_links:
            book_url = urljoin(categorie_url, book['href'])
            book_soup = get_soup(book_url)
            
            # récupération de l'url de l'image à télécharger
            image_url = get_image_url(book_soup)
            image_file = get_image_file(image_url)

            #construit le chemin et le titre de sauvegarde pour l'image
            # défini la catégorie pour la sauvegarde des données
            category_name = get_category(book_soup)


            # Construit le chemin de sauvegarde pour l'image, nettoie uniquement le titre du livre
            MAX_TITLE_LENGTH = 100 #limite la longueur des caractères dans le titre/nom de fichier selon les restrictions windows
            book_title_cleaned = clean_filename(get_title(book_soup))[:MAX_TITLE_LENGTH]
            image_save_path = os.path.join('book_images', category_name, f"{book_title_cleaned}.jpg")
            
            #Sauvegarde l'image si les données sont récupérées
            if image_file:
                save_image_file(image_file, image_save_path)
            
            data = {
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
            print(data)
            data_list.append(data)
        


        
        # Sauvegarde les données de la catégorie actuelle une 
        #fois tous les livres de la page (et potentiellement de la pagination) traités
        save_to_csv_by_category(data_list, category_name)
        
        # Gestion de la pagination
        next_button = soup.find(class_='next')
        if next_button:
            next_page_partial = next_button.find('a')['href']
            categorie_url = urljoin(categorie_url, next_page_partial)
        else:
            break

# Sauvegarde en dehors des boucles pour éviter les écritures multiples           
#save_to_csv(data_list, 'all_data.csv')
