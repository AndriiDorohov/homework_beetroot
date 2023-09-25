# Task 2

# Requests using concurrent and multiprocessing libraries

# Download all comments from a subreddit of your choice using
# URL: https://api.pushshift.io/reddit/comment/search/ .

# As a result, store all comments in chronological order in JSON and dump it to a file.
# For this task use concurrent and multiprocessing libraries for making requests to Reddit API.


# Код отримує по запиту до API 70 фільмів. Використовує потоки при запиті. Потім сортує за країною
# походження і записує до файлу. Поле "original_language" - містить країну закодовану двома символами

import threading
import requests
import json

BASE_URL = "https://api.themoviedb.org/3/"
API_KEY = "d2f58f193ec10f64760e31baa52fd192"  # My API Key

movies_data = []


def fetch_movies(count=70):
    page = 1
    results = []

    while len(results) < count:
        url = f"{BASE_URL}discover/movie?api_key={API_KEY}&language=en-US&page={page}"
        response = requests.get(url)
        data = response.json()
        movies = data.get("results", [])

        for movie in movies:
            results.append(movie)
            if len(results) >= count:
                break
        page += 1

    return results


def fetch_and_extend_movies():
    global movies_data
    movies_data.extend(fetch_movies())


def sort_movies_by_country(movies):
    filtered_movies = [movie for movie in movies if movie.get("original_language")]
    sorted_movies = sorted(filtered_movies, key=lambda x: x.get("original_language"))
    return sorted_movies


def write_to_json_file(data, filename):
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    movies_thread = threading.Thread(target=fetch_and_extend_movies)
    movies_thread.start()
    movies_thread.join()

    sorted_movies = sort_movies_by_country(movies_data)
    write_to_json_file(sorted_movies, "sorted_movies.json")
