# AI-Powered Web Scraping Tools Collection

A modern web scraping toolkit that combines traditional scraping methods with AI capabilities. This project provides a Streamlit-based UI for easy interaction with various scraping tools including BeautifulSoup, FireCrawl, Jina.ai Reader, and ScrapeGraphAI.

## Features

### 1. Basic Scraper
- HTML content extraction using BeautifulSoup4
- Structured data extraction including:
  - Headings (H1, H2, H3)
  - Paragraphs
  - Links
- JSON output format
- Custom CSS selector support

### 2. FireCrawl Scraper
- Asynchronous web crawling
- Structured data extraction
- Progress tracking
- Custom parameter support

### 3. Jina.ai Reader
- AI-powered content extraction
- Text summarization
- Image extraction with captions
- Multiple output formats

### 4. ScrapeGraphAI
- Multiple scraping modes:
  - SMART_SCRAPER
  - SEARCH
  - OMNI_SCRAPER
- GPT-3.5 integration
- Custom prompt support

## Installation

1. Clone the repository:
```bash
git clone https://github.com/imanoop7/Web-Scrapping-Tool-for-AI
cd Web-Scrapping-Tool-for-AI
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run streamlit_app.py
```

2. In the web interface:
   - Enter the URL to scrape
   - Select your preferred scraping method
   - Configure any additional parameters
   - Click "Start Scraping"

3. View and download results in JSON format

## Required API Keys

Store your API keys securely. The following APIs are required for full functionality:

- FireCrawl API key
- Jina.ai API key
- OpenAI API key (for ScrapeGraphAI)

## Dependencies

- Python 3.8+
- streamlit
- requests
- beautifulsoup4
- pydantic
- aiohttp
- asyncio
- typing-extensions

## Project Structure

```
├── streamlit_app.py      # Main Streamlit application
├── basic_scraper.py      # BeautifulSoup-based scraper
├── firecrawl_scraper.py  # FireCrawl integration
├── jina_reader.py        # Jina.ai Reader integration
├── scrapegraph_ai.py     # ScrapeGraphAI implementation
└── requirements.txt      # Project dependencies
```

## Features by Scraper

### Basic Scraper
- Content extraction:
  - Headings (H1, H2, H3)
  - Paragraphs (with length filtering)
  - Links with text and URLs
- Custom selector support
- JSON output with timestamp
- Error handling and validation

### FireCrawl Scraper
- Asynchronous operation
- Progress tracking
- Structured data extraction
- Custom parameter support

### Jina Reader
- URL content extraction
- Text summarization
- Image extraction
- Error handling

### ScrapeGraphAI
- Multiple graph types
- GPT-3.5 integration
- Custom prompts
- Image processing support

## Best Practices

1. Rate Limiting
   - Implement appropriate delays between requests
   - Respect website robots.txt

2. Error Handling
   - All scrapers include comprehensive error handling
   - Validation of API keys and inputs

3. Data Management
   - Results saved in structured JSON format
   - Timestamp-based file naming
   - Download functionality for results

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


