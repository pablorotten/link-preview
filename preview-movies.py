import requests
from bs4 import BeautifulSoup

# Function to extract the movie data
def get_movie_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract title
    title = soup.find('h1', {'id': 'main-title'})
    title = title.get_text(strip=True) if title else 'Title Not Found'

    # Extract year (if it exists)
    year = soup.find('dd', class_='movie-info')
    year = year.get_text(strip=True) if year else 'Year Not Found'

    # Extract director (if it exists)
    director = soup.find('span', itemprop='director')
    director = director.get_text(strip=True) if director else 'Director Not Found'

    # Extract rating (if it exists)
    rating = soup.find('div', {'class': 'avg-rating'})
    rating = rating.get_text(strip=True) if rating else 'Rating Not Found'

    return {'title': title}

# Step 1: Read links from the file called "links"
with open('links', 'r') as file:
    links = [line.strip() for line in file if line.strip()]

# Step 2: Extract movie data for each link
movies = [get_movie_info(link) for link in links]

# Step 3: Write the movie data to a file called "movies"
with open('movies', 'w') as file:
    for movie in movies:
        file.write(f"{movie['title']}\n")

print("Movie information has been successfully written to the 'movies' file.")