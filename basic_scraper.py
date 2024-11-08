import requests
from bs4 import BeautifulSoup
import json
from typing import Dict, List, Any
from datetime import datetime

class BasicScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def scrape_webpage(self, url: str, article_selector: str = None) -> Dict[str, Any]:
        try:
            # Send GET request
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Initialize results dictionary
            scraped_data = {
                "url": url,
                "timestamp": datetime.now().isoformat(),
                "content": {
                    "headings": [],
                    "paragraphs": [],
                    "links": []
                }
            }
            
            # Extract content based on selector
            if article_selector:
                elements = soup.select(article_selector)
                if elements:
                    scraped_data["content"]["custom_selector"] = [
                        elem.get_text(strip=True) for elem in elements if elem.get_text(strip=True)
                    ]
            
            # Extract headings
            for heading in soup.find_all(['h1', 'h2', 'h3']):
                text = heading.get_text(strip=True)
                if text:
                    scraped_data["content"]["headings"].append({
                        "type": heading.name,
                        "text": text
                    })
            
            # Extract paragraphs
            for para in soup.find_all('p'):
                text = para.get_text(strip=True)
                if text and len(text) > 20:  # Filter out short texts
                    scraped_data["content"]["paragraphs"].append(text)
            
            # Extract links
            for link in soup.find_all('a'):
                href = link.get('href')
                text = link.get_text(strip=True)
                if href and text:
                    scraped_data["content"]["links"].append({
                        "text": text,
                        "url": href
                    })
            
            return scraped_data
            
        except requests.RequestException as e:
            return {
                "error": f"Request error: {str(e)}",
                "url": url,
                "success": False
            }
        except Exception as e:
            return {
                "error": f"Unexpected error: {str(e)}",
                "url": url,
                "success": False
            }