from typing import Dict, Any, List, Optional
from enum import Enum

class GraphType(Enum):
    SMART_SCRAPER = "smart_scraper"
    SEARCH = "search"
    SPEECH = "speech"
    SCRIPT_CREATOR = "script_creator"
    OMNI_SCRAPER = "omni_scraper"

class ScrapeGraphAI:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.validate_config()

    def validate_config(self):
        """Validate the configuration"""
        required_keys = ["llm"]
        if not all(key in self.config for key in required_keys):
            raise ValueError(f"Configuration must contain: {required_keys}")
        
        # Validate LLM config
        llm_config = self.config["llm"]
        if "api_key" not in llm_config or not llm_config["api_key"]:
            raise ValueError("OpenAI API key is required in llm configuration")

    def create_graph(self, graph_type: GraphType, **kwargs):
        """Create a specific type of scraping graph"""
        if graph_type == GraphType.SMART_SCRAPER:
            return self._create_smart_scraper(**kwargs)
        elif graph_type == GraphType.SEARCH:
            return self._create_search_graph(**kwargs)
        elif graph_type == GraphType.OMNI_SCRAPER:
            return self._create_omni_scraper(**kwargs)
        else:
            raise ValueError(f"Unsupported graph type: {graph_type}")

    def _create_smart_scraper(self, url: str, prompt: str) -> Dict[str, Any]:
        """Create a SmartScraperGraph instance"""
        return {
            "type": "smart_scraper",
            "url": url,
            "prompt": prompt,
            "config": self.config
        }

    def _create_search_graph(self, prompt: str, max_results: int = 5) -> Dict[str, Any]:
        """Create a SearchGraph instance"""
        return {
            "type": "search",
            "prompt": prompt,
            "max_results": max_results,
            "config": self.config
        }

    def _create_omni_scraper(self, url: str, prompt: str) -> Dict[str, Any]:
        """Create an OmniScraperGraph instance"""
        return {
            "type": "omni_scraper",
            "url": url,
            "prompt": prompt,
            "config": self.config,
            "image_processing": True
        }

    def execute_graph(self, graph: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the created graph and return results"""
        # Simulate graph execution
        return {
            "status": "success",
            "graph_type": graph["type"],
            "results": {
                "extracted_data": "Sample extracted data",
                "metadata": {
                    "url": graph.get("url"),
                    "prompt": graph.get("prompt")
                }
            }
        }