# Task 2

# Requests using asyncio and aiohttp

# Download all comments from a subreddit of your choice using
# URL: https://api.pushshift.io/reddit/comment/search/ .

# As a result, store all comments in chronological order in
# JSON and dump them to a file. For this task use asyncio and
# aiohttp libraries for making requests to Reddit API.

import asyncio
import aiohttp
import json

BASE_URL = "https://api.themoviedb.org/3/"
API_KEY = "d2f58f193ec10f64760e31baa52fd192"

movies_data = []


async def fetch_movies(session, count=70):
    page = 1
    results = []

    while len(results) < count:
        url = f"{BASE_URL}discover/movie?api_key={API_KEY}&language=en-US&page={page}"
        async with session.get(url) as response:
            data = await response.json()
            movies = data.get("results", [])

            for movie in movies:
                results.append(movie)
                if len(results) >= count:
                    break
        page += 1

    return results


async def fetch_and_extend_movies():
    async with aiohttp.ClientSession() as session:
        global movies_data
        movies_data.extend(await fetch_movies(session))


def sort_movies_by_country(movies):
    filtered_movies = [movie for movie in movies if movie.get("original_language")]
    sorted_movies = sorted(filtered_movies, key=lambda x: x.get("original_language"))
    return sorted_movies


def write_to_json_file(data, filename):
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


async def main():
    await fetch_and_extend_movies()

    sorted_movies = sort_movies_by_country(movies_data)
    write_to_json_file(sorted_movies, "sorted_movies.json")


if __name__ == "__main__":
    asyncio.run(main())
