import requests 
from bs4 import BeautifulSoup
import csv



"""
● product_page_url
● universal_ product_code (upc)
● title
● price_including_tax
● price_excluding_tax
● number_available
● product_description
● category
● review_rating
● image_url


"""

#Extraction des données d'un livre

url = 'https://books.toscrape.com/catalogue/i-had-a-nice-time-and-other-lies-how-to-find-love-sht-like-that_814/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
product_page_url = url
universal_product_code = soup.find_all('tr')[0].td.text
title = soup.find('h1').get_text(strip=True)
price_including_tax = price_including_tax = soup.find_all('tr')[3].td.text.strip()[1:]
price_excluding_tax = price_including_tax = soup.find_all('tr')[2].td.text.strip()[1:]
num_available_raw = soup.find_all('tr')[5].td.text
num_available = num_available_raw.replace('In stock', '').replace('(', '').replace(')', '').replace('available', '').strip()
product_description = soup.find('div', id='product_description').find_next_sibling('p').text
category = soup.find('ul', class_='breadcrumb').find_all('a')[2].text.strip()
review_rating = soup.find_all('tr')[6].td.text
star_rating = soup.find('p', class_='star-rating')['class'][1]
base_url ='https://books.toscrape.com/'
image_url = soup.find('img')['src'].replace('../../', base_url)

data ={
    'product_page_url':product_page_url, 
    'universal_product_code': universal_product_code,
    'title':title,
    'price_including_tax' : price_including_tax,
    'price_excluding_tax': price_excluding_tax,
    'num_available' : num_available,
    'product_description': product_description,
    'category':category,
    'review_rating': review_rating,
    'star_rating':star_rating,
    'image_url':image_url

}
print(data)

with open('single_book.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=data.keys())
    writer.writeheader()
    writer.writerow(data)


