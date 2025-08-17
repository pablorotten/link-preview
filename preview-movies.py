import requests
from bs4 import BeautifulSoup

# Function to extract the movie data
def get_movie_info(url):
    # Add a User-Agent header to mimic a real browser visit
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')

        # --- MODIFIED SECTION ---
        # Find the <dt> tag that specifically contains "Título original"
        original_title_dt = soup.find('dt', string='Título original')
        
        # If that tag is found, get the text from the next element, which is the <dd> tag
        if original_title_dt:
            title_element = original_title_dt.find_next_sibling('dd')
            title = title_element.get_text(strip=True) if title_element else 'Original Title Not Found'
        else:
            # Fallback to the main title if "Título original" isn't found
            title_element = soup.select_one('h1#main-title span[itemprop="name"]')
            title = title_element.get_text(strip=True) if title_element else 'Title Not Found'
        # --- END OF MODIFIED SECTION ---

        return {'title': title}

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return {'title': 'Error Fetching URL'}

# Step 1: Read links from the file called "links"
try:
    with open('links', 'r') as file:
        links = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    print("Error: 'links' file not found. Please create it and add your URLs.")
    links = []

# Step 2: Extract movie data for each link
if links:
    movies = [get_movie_info(link) for link in links]

    # Step 3: Write the movie data to a file called "movies"
    with open('movies', 'w', encoding='utf-8') as file:
        for movie in movies:
            file.write(f"{movie['title']}\n")

    print("Movie information has been successfully written to the 'movies' file.")