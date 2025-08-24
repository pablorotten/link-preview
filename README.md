# Link preview for Filmaffinity movies

| 🇬🇧 Input a list of Filmaffinity movies links       | ➡️ | Output the movies title                           |
| -------------------------------------------------- | -- | ------------------------------------------------- |
| 🇪🇸 Introduce una lista con enlaces de Filmaffinity | ➡️ | Genera una lista con los títulos de las películas |

## Setup

```sh
python3 -m venv venv
source venv/bin/activate
pip3 install requests
pip3 install requests beautifulsoup4
```

## Run it!

```sh
python3 preview-movies.py
```

> [!CAUTION]
> This script uses [scraping](https://en.wikipedia.org/wiki/Web_scraping)!

## Useful commands

```sh
# find lines in `links` that are not in `added-links` and the opposite
grep -v -F -f added-links links
grep -F -x -f added-links links

# find links of movies not found
awk 'NR==FNR {if ($0 == "Title Not Found") lines[FNR]; next} FNR in lines' movies link

# Group movies in 16
awk '1; NR % 16 == 0 {print ""}' added-movies > movies_grouped.txt
```