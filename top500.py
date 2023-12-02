import random
# import telebot
# import config
from bs4 import BeautifulSoup as bs
import requests

def spisok_500(url_500_1, url_500_2, teg_500, class_500, teg_genre_500, class_genre_500):
    spisok_films_500_name = []
    spisok_films_500_genre = []
    films_500_dict = {}
    if len(spisok_films_500_name) == 0:
        for i in range (1, 5):
            responce_get_name = requests.get(f'{url_500_1}{i}{url_500_2}')
            soup_name = bs(responce_get_name.text, 'html.parser')
            quotes_film_name = soup_name.find_all(teg_500, class_=class_500)
            responce_get_genre = requests.get(f'{url_500_1}{i}{url_500_2}')
            soup_genre = bs(responce_get_genre.text, 'html.parser')
            quotes_film_genre = soup_genre.find_all(teg_genre_500, class_=class_genre_500)
            # responce_get_foto = requests.get(f'{url_500_1}{i}{url_500_2}')
            # soup_foto = bs(responce_get_foto.content, 'html.parser')
            # quotes_film_foto = soup_foto.find_all('img', teg_foto_500, class_=class_foto_500)
            for film in quotes_film_name:
                spisok_films_500_name.append(film.text)
            for film in quotes_film_genre:
                spisok_films_500_genre.append(film.text)
            films_500_dict = dict(zip(spisok_films_500_name, spisok_films_500_genre))
        a = random.choice(spisok_films_500_name)
        b = f'{a}, {films_500_dict[a]}'
        return b
    else:
        a = random.choice(spisok_films_500_name)
        b = f'{a}, {films_500_dict[a]}'
        return b
