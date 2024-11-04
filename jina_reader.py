import requests
from typing import Optional, Dict, Any, List

class JinaReader:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("Jina API key is required")
        self.api_key = api_key
        self.base_url = "https://r.jina.ai"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def read_url(self, url: str) -> Dict[str, Any]:
        """
        Extract content from a URL using Jina Reader API
        """
        try:
            response = requests.get(
                f"{self.base_url}/read",
                params={"url": url},
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error reading URL: {e}")
            return {}

    def summarize(self, text: str, max_length: Optional[int] = None) -> str:
        """
        Summarize text content using Jina Reader API
        """
        try:
            data = {
                "text": text,
                "max_length": max_length
            }
            response = requests.post(
                f"{self.base_url}/summarize",
                json=data,
                headers=self.headers
            )
            response.raise_for_status()
            return response.json().get("summary", "")
        except requests.RequestException as e:
            print(f"Error summarizing text: {e}")
            return ""

    def extract_images(self, url: str) -> List[Dict[str, str]]:
        """
        Extract images with captions from a URL
        """
        try:
            response = requests.get(
                f"{self.base_url}/images",
                params={"url": url},
                headers=self.headers
            )
            response.raise_for_status()
            return response.json().get("images", [])
        except requests.RequestException as e:
            print(f"Error extracting images: {e}")
            return []