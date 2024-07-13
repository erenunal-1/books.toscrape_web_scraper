import pandas as pd
import requests
from bs4 import BeautifulSoup

class BookScraper:
    BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
    HOME_URL = "https://books.toscrape.com"

    def __init__(self):
        self.total_pages = self.get_total_pages()
        self.books = []

    def get_total_pages(self):
        """
        Returns the total number of pages available on the website.

        This method sends a GET request to the homepage of the website, parses the content using BeautifulSoup,
        and extracts the total page number from the HTML element representing the current page.
        The total page number is obtained by extracting the last part of the page information text.
    
        Returns:
            int: The total number of pages available on the website.
        """
        try:
            response = requests.get(self.HOME_URL)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching total pages: {e}")
            return 0

        soup = BeautifulSoup(response.content, "html.parser")
        page_info = soup.find('li', class_='current').text.strip()
        total_pages = int(page_info.split()[-1])
        return total_pages

    def scrape(self):
        """
        Scrape book information from each page of the website.

        This method iterates through each page of the website to scrape information about books.
        It sends a GET request to each page, parses the content with BeautifulSoup, and extracts
        details such as title, star rating, and price of each book.

        After extraction, the collected book data is stored in the 'books' list attribute of the object.

        Returns:
            None
        """
        for i in range(1, self.total_pages + 1):
            url = self.BASE_URL.format(i)
            try:
                response = requests.get(url)
                response.raise_for_status()
            except requests.RequestException as e:
                print(f"Error fetching page {i}: {e}")
                continue

            soup = BeautifulSoup(response.content, "html.parser")
            articles = soup.find_all('article', class_='product_pod')

            for article in articles:
                try:
                    title = article.find('img')['alt']
                    star = article.find('p', class_='star-rating')['class'][1]
                    price = article.find('p', class_='price_color').text
                    price = float(price[1:])
                    self.books.append([title, price, star])
                except (AttributeError, ValueError, TypeError) as e:
                    print(f"Error parsing book information: {e}")

    def get_books(self):
        """
        Retrieve the list of scraped book information.

        This method returns the list of book information that has been scraped and stored
        in the 'books' attribute of the object.

        Returns:
            list: A list containing the scraped book information.
        """
        return self.books

    def to_dataframe(self):
        """
        Convert scraped book information to a pandas DataFrame.

        This method converts the scraped book information stored in the 'books' attribute
        of the object into a pandas DataFrame. It creates a DataFrame with columns for
        book title, price, and star rating.

        Returns:
            pandas.DataFrame: A DataFrame containing the scraped book information.
        """
        return pd.DataFrame(self.books, columns=['Title', 'Price', 'Star Rating'])


if __name__ == "__main__":
    scraper = BookScraper()
    scraper.scrape()
    books_df = scraper.to_dataframe()
    print(books_df.head())
