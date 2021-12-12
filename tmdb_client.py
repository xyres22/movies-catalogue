import requests
import random
api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3OWUwNzkzMjZlNGNkZjgxZTg5NTYwYzllMDhlZjJlZiIsInN1YiI6IjYxOTUwYWRhZjkwYjE5MDAyOTk2OGFlOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LcL7o6NbhCTVIKIqmZ1j7G9fAUInn28TAKCSRRNL6dE"
def get_headers():
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    return headers


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = get_headers()
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = get_headers()
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id, how_many):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = get_headers()
    response = requests.get(endpoint, headers=headers)
    return response.json()['cast'][:how_many]

def get_movie_images(movie_id):
    endpoint = f'https://api.themoviedb.org/3/movie/{movie_id}/images'
    headers = get_headers()
    response = requests.get(endpoint, headers=headers)
    data = response.json()
    data = random.choice(data['backdrops'])
    return data

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = get_headers()
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies(how_many, list_type = 'popular'):
    data = get_movies_list(list_type)
    random.shuffle(data['results'])
    return data["results"][:how_many]



