# Books to Scrape - Price Tracker

Ce projet développe un système automatisé pour surveiller et enregistrer les prix des livres d'occasion sur [Books to Scrape](https://books.toscrape.com/), une librairie en ligne. Utilisant Python et BeautifulSoup, le script extrait les détails des produits tels que le titre, le prix, la disponibilité, et l'image, pour chaque livre listé. Conçu pour aider *Books Online* à rester compétitif, ce tracker est un outil clé pour l'analyse de marché en temps réel.

## Fonctionnalités

- Extraction des informations de produits **par catégorie**.
- Navigation automatique à travers la **pagination**.
- Enregistrement des données dans des **fichiers CSV par catégorie**.
- Téléchargement et sauvegarde des **images des couvertures de livres**.

## Installation

Instructions pour configurer l'environnement, installer les dépendances, et exécuter le script.

### Prérequis

- Python 3.9+
- BeautifulSoup4
- Requests

### Configuration de l'environnement à partir du terminal

1. Clonez le dépôt GitHub :
  ```
  git clone https://github.com/hericlibong/Books-to-scrape-prices-tracker.git
  ```

2. Allez dans dossier du projet
  ```
  cd Books-to-scrape-prices-tracker
  ```

3. Installez un environnement virtuel :
  ```
  python -m venv venv
  ```

4. Activez l'environnement virtuel :
- Sur Windows :
  ```
  venv\Scripts\activate
  ```
- Sur MacOS/Linux :
  ```
  source venv/bin/activate
  ```

5. Installez les dépendances :
  ```
  pip install -r requirements.txt
  ```


## Utilisation

Détails sur comment lancer le script pour récupérer les données.

1. Aller dans le dossier du scraper :
  ```
  cd BOOKS-TO-SCRAPE
  ```

Pour lancer le script, exécutez dans le terminal :


``` 
python main.py
```
---

Pour toute question ou suggestion, n'hésitez pas à ouvrir un issue dans le dépôt GitHub.


