# Web Scraping Tools Collection

A collection of modern web scraping tools leveraging different AI and automation approaches. This repository includes implementations of various scraping methods using BeautifulSoup, FireCrawl, Jina.ai Reader, and ScrapeGraphAI.

## Features

- **Basic Scraper**: Simple web scraping using BeautifulSoup4
- **FireCrawl Scraper**: Asynchronous web crawling with structured data extraction
- **Jina.ai Reader**: AI-powered content extraction and summarization
- **ScrapeGraphAI**: Advanced AI-based scraping with multiple specialized modes

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
## Required API Keys

To use all features of this collection, you'll need:
- FireCrawl API key
- Jina.ai API key
- OpenAI API key (for ScrapeGraphAI)

## Dependencies

- Python 3.8+
- requests >= 2.31.0
- beautifulsoup4 >= 4.12.0
- pydantic >= 2.5.0
- aiohttp >= 3.9.0
- asyncio >= 3.4.3
- typing-extensions >= 4.8.0

## Important Notes

1. **API Keys**: Replace all `your_api_key` placeholders with actual API keys
2. **Rate Limiting**: Add appropriate delays between requests to avoid rate limiting
3. **Terms of Service**: Always respect websites' robots.txt and terms of service
4. **Error Handling**: Implement proper error handling for production use

## Best Practices

1. Always check a website's robots.txt before scraping
2. Implement rate limiting to avoid overwhelming servers
3. Use appropriate error handling and logging
4. Keep API keys secure and never commit them to version control
5. Consider using proxy rotation for large-scale scraping

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
