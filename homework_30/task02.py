# Task 2

# Load data

# Download all comments from a subreddit of your choice using
# URL: https://api.pushshift.io/reddit/comment/search/ .

# As a result, store all comments in chronological order in
# JSON and dump it to a file.

import requests
from bs4 import BeautifulSoup

r = requests.get("https://jsonplaceholder.typicode.com/")
incom_html = r.text

parsed_html = BeautifulSoup(incom_html, 'html.parser')
new_html = parsed_html.prettify()


with open('temp.html', 'w', encoding='utf-8') as file:
    file.write(new_html)
