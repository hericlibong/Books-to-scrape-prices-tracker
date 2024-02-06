from bs4 import BeautifulSoup
import requests
import re


# -----  Fonctions de récupération des données ------

def get_soup(url):
    """ 
    Fait une requête HTTP GET à l'URL spécifiée et retourne un objet BeautifulSoup du contenu HTML.
    
    Args:
        url (str): URL de la page à récupérer.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie le succès de la requête
        return BeautifulSoup(response.content, 'html.parser')
    except requests.RequestException as e:
        print(f"Erreur lors de la récupération de l'URL {url}: {e}")
        return None
    
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


def get_category(soup):
    """Extrait la catégorie du produit """
    try : 
       return soup.find('ul', class_='breadcrumb').find_all('a')[2].text.strip()
    except Exception:
        return None

def get_universal_product_code(soup):
    """ Extrait le code produit universel (UPC) de la page du produit."""
    try: 
        return soup.find_all('tr')[0].td.text
    except Exception:
        return None


def get_title(soup):
    """ Extrait le titre du livre de la page du produit. """
    try :
        return soup.find('h1').text
    except Exception:
        return None


def get_price_including_tax(soup):
    """
    Extrait le prix du livre incluant les taxes
    
    Returns:
        float: Prix incluant les taxes ou None en cas d'erreur.
    """
    try:
        price_including_tax = soup.find_all('tr')[3].td.text.strip()[1:] #Enlève le sigle Livre sur le prix
        return float(price_including_tax)
    except Exception:
        return None

def get_price_excluding_tax(soup):
    """
        Extrait le prix du livre hors taxes.
       
       Returns:
            float: Prix hors taxes ou None en cas d'erreur.
    """
    try : 
        price_excluding_tax = soup.find_all('tr')[2].td.text.strip()[1:] 
        return float(price_excluding_tax)
    except Exception:
        return None

def get_number_available(soup):
    """ 
        Extrait le nombre d'exemplaires disponibles du produit.
        
        Returns:
        int: Nombre d'exemplaires disponibles ou None en cas d'erreur.
    """
    try : 
        num_available_raw = soup.find_all('tr')[5].td.text
        num_available = num_available_raw.replace('In stock', '').replace('(', '').replace(')', '').replace('available', '').strip()
        return int(num_available)
    except Exception:
        return None 

def get_star_rating(soup):
    """
    Extrait la note du produit sous forme d'étoiles et la convertit en nombre.
    
    Returns:
        int: Note sous forme de nombre ou 0 en cas d'absence de note.
    """
    words_to_nums = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5} # Dictionnaire pour convertir les mots en chiffre
    try : 
        rating_word = soup.find('p', class_='star-rating')['class'][1]
        # Convertir le mot en nombre en utilisant le dictionnaire
        return words_to_nums.get(rating_word, 0)  #Retourne la valeur de la clé si celle-ci est dans le dictionnaire. Si la clé n'est pas présente, la valeur est 0
    except Exception:
        return None  
    

def get_product_description(soup):
    """Extrait la description du produit de la page."""

    try :
        description_tag = soup.find('div', id='product_description')
        if description_tag : 
            description = description_tag.find_next_sibling('p').text
            description = description.replace('/', '')
            description = description.replace('&amp;', '&')
            description = re.sub(' +', ' ', description)
            description = description.strip()
            return description
        else:
            return None
    except Exception:
        return None 
 
def get_image_url(soup):
    """Construit l'URL complète de l'image du produit."""
    base_url = 'https://books.toscrape.com/'
    try :
        return soup.find('img')['src'].replace('../../', base_url)
    except Exception:
        return None 
    
# ----- Récupération des images -------
    
def get_image_file(image_url):
    """ 
    Télécharge les données binaires de l'image à partir de l'URL spécifiée.
    
    Args:
        image_url (str): URL de l'image à télécharger.
    
    
    Returns:
        bytes: Données binaires de l'image ou None en cas d'erreur.
    
    """
    try :
        response = requests.get(image_url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print(f"Erreur lors du téléchargement de l'image : {e}")
        return None