# Task 1

# Robots.txt

# Download and save to file robots.txt from wikipedia, twitter websites etc.

import requests

r = requests.get("https://www.wikipedia.org/robots.txt", stream=True)
print(r.content)

with open('robots.txt', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
