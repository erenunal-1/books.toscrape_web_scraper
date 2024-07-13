# Books to Scrape

This project is a web scraping tool to extract book information from the website [Books to Scrape](https://books.toscrape.com). The tool scrapes book titles, prices, and star ratings, and stores the data in a pandas DataFrame.

![Books to Scrape Homepage](homepage_screenshot.png)

## Features

- Scrapes book information (title, price, star rating) from each page of the website.
- Converts the scraped data into a pandas DataFrame for further analysis.
- Handles multiple pages by dynamically finding the total number of pages.
- Includes error handling for network requests and data extraction.

## Setup and Usage

### Requirements
- Python 3.6 or higher
- Required Python packages listed in `requirements.txt`

### Installation

1. Clone the repository:

```sh
git clone https://github.com/erenunal-1/books.toscrape_web_scraper.git
cd books.toscrape_web_scraper
```

2. Install the required packages:

```sh
pip install -r requirements.txt
```

## Running the Script

```sh
python book_scraper.py
```

## Sample Output

| Title                                   | Price | Star Rating |
|-----------------------------------------|-------|-------------|
| A Light in the Attic                    | 51.77 | Three       |
| Tipping the Velvet                      | 53.74 | One         |
| Soumission                              | 50.10 | One         |
| Sharp Objects                           | 47.82 | Four        |
| Sapiens: A Brief History of Humankind   | 54.23 | Five        |

## License
This project is licensed under the [MIT License](https://github.com/erenunal-1/books.toscrape_web_scraper/blob/main/LICENSE) - see the LICENSE file for details.
