import cloudscraper # Changed from 'requests'
from bs4 import BeautifulSoup

# Function to extract the movie data
def get_movie_info(url):
    # cloudscraper manages the headers and cookies needed to bypass bot detection
    scraper = cloudscraper.create_scraper()
    
    try:
        # Use the scraper instead of requests.get()
        response = scraper.get(url) 
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')

        # --- Your parsing logic remains the same ---
        original_title_dt = soup.find('dt', string='Título original')
        
        if original_title_dt:
            title_element = original_title_dt.find_next_sibling('dd')
            title = title_element.get_text(strip=True) if title_element else 'Original Title Not Found'
        else:
            title_element = soup.select_one('h1#main-title span[itemprop="name"]')
            title = title_element.get_text(strip=True) if title_element else 'Title Not Found'

        return {'title': title}

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return {'title': 'Error Fetching URL'}

# --- The rest of your script remains the same ---

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