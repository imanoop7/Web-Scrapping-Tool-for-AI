import requests
from bs4 import BeautifulSoup
import csv

class BasicScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def scrape_webpage(self, url, article_class='article-title'):
        try:
            # Send GET request
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract titles
            titles = soup.find_all('h2', class_=article_class)
            
            # Store results
            results = [title.text.strip() for title in titles]
            
            # Save to CSV
            self._save_to_csv(results)
            
            return results
            
        except requests.RequestException as e:
            print(f"Error fetching webpage: {e}")
            return []

    def _save_to_csv(self, titles, filename='article_titles.csv'):
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Title"])  # Header
                for title in titles:
                    writer.writerow([title])
            print(f"Data saved to {filename}")
        except IOError as e:
            print(f"Error saving to CSV: {e}")

if __name__ == "__main__":
    scraper = BasicScraper()
    results = scraper.scrape_webpage("https://example.com/news")
    print("Scraped titles:", results) 