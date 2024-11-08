import streamlit as st
import asyncio
from jina_reader import JinaReader
from firecrawl_scraper import FireCrawlScraper
from basic_scraper import BasicScraper
from scrapegraph_ai import ScrapeGraphAI, GraphType
import json
import os
from datetime import datetime

# Initialize session state for API keys
if 'api_keys' not in st.session_state:
    st.session_state.api_keys = {
        'jina': '',
        'firecrawl': '',
        'openai': ''
    }

def init_page():
    st.set_page_config(
        page_title="AI Web Scraping Tools",
        page_icon="🌐",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.title("🌐 AI Web Scraping Tools")

def handle_api_keys():
    """Handle API keys in sidebar"""
    with st.sidebar:
        st.header("🔑 API Key Management")
        
        # Add expander for API key inputs
        with st.expander("Configure API Keys"):
            st.session_state.api_keys['jina'] = st.text_input(
                "Jina API Key",
                type="password",
                value=st.session_state.api_keys['jina']
            )
            st.session_state.api_keys['firecrawl'] = st.text_input(
                "FireCrawl API Key",
                type="password",
                value=st.session_state.api_keys['firecrawl']
            )
            st.session_state.api_keys['openai'] = st.text_input(
                "OpenAI API Key",
                type="password",
                value=st.session_state.api_keys['openai']
            )

def save_results(results, scraper_type):
    """Save results with timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"results_{scraper_type}_{timestamp}.json"
    
    # Create results directory if it doesn't exist
    os.makedirs("results", exist_ok=True)
    filepath = os.path.join("results", filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4)
    return filepath

def display_results(results, scraper_type):
    """Display results and download button"""
    st.success("✅ Scraping completed successfully!")
    
    # Display results in tabs
    tab1, tab2 = st.tabs(["📊 Formatted Results", "📝 Raw JSON"])
    
    with tab1:
        if scraper_type == "Basic Scraper":
            # Display headings
            if "content" in results and "headings" in results["content"]:
                st.write("### 📑 Headings")
                for heading in results["content"]["headings"]:
                    st.write(f"{heading['type'].upper()}: {heading['text']}")
            
            # Display paragraphs
            if "content" in results and "paragraphs" in results["content"]:
                st.write("### 📝 Paragraphs")
                for idx, para in enumerate(results["content"]["paragraphs"], 1):
                    with st.expander(f"Paragraph {idx}"):
                        st.write(para)
            
            # Display links
            if "content" in results and "links" in results["content"]:
                st.write("### 🔗 Links")
                for link in results["content"]["links"]:
                    st.write(f"- [{link['text']}]({link['url']})")
        else:
            st.write("### Extracted Data")
            st.write(results)
    
    with tab2:
        st.json(results)
    
    # Create download button for JSON
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"scraped_data_{timestamp}.json"
    
    # Convert results to JSON string
    json_str = json.dumps(results, indent=2)
    
    # Create download button
    st.download_button(
        label="📥 Download JSON",
        data=json_str,
        file_name=filename,
        mime="application/json",
    )

def run_basic_scraper(url, article_selector):
    with st.spinner("🔍 Scraping webpage..."):
        try:
            scraper = BasicScraper()
            results = scraper.scrape_webpage(url, article_selector)
            
            if "error" in results:
                st.error(f"Scraping error: {results['error']}")
                return results
            
            if not any(results["content"].values()):
                st.warning("No content was extracted. Try adjusting the selector or check if the website allows scraping.")
            
            return results
            
        except Exception as e:
            st.error(f"Error during scraping: {str(e)}")
            return {"error": str(e), "success": False}

async def run_firecrawl(url, api_key):
    with st.spinner("🔄 Processing with FireCrawl..."):
        scraper = FireCrawlScraper(api_key)
        results = await scraper.scrape_url_async(url)
        status = await scraper.check_crawl_status(results['crawl_id'])
        return {"crawl_results": results, "status": status}

def run_jina_reader(url, api_key, action, max_length=None):
    with st.spinner("🤖 Processing with Jina AI..."):
        reader = JinaReader(api_key)
        if action == "Read URL":
            return reader.read_url(url)
        elif action == "Summarize":
            content = reader.read_url(url)
            if content.get("text"):
                return {"summary": reader.summarize(content["text"], max_length)}
        else:  # Extract Images
            return {"images": reader.extract_images(url)}

def run_scrapegraph(url, api_key, graph_type, prompt):
    with st.spinner("🎯 Processing with ScrapeGraphAI..."):
        config = {
            "llm": {
                "model": "gpt-3.5-turbo",
                "temperature": 0.7,
                "api_key": api_key
            }
        }
        scraper = ScrapeGraphAI(config)
        graph = scraper.create_graph(
            GraphType[graph_type],
            url=url,
            prompt=prompt
        )
        return scraper.execute_graph(graph)

def validate_api_key(key_name: str) -> bool:
    """Validate if an API key is present"""
    if not st.session_state.api_keys.get(key_name):
        st.error(f"⚠️ {key_name.capitalize()} API Key is required")
        return False
    return True

def main():
    init_page()
    handle_api_keys()
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        url = st.text_input("🔗 Enter URL to scrape", "https://example.com")
    
    with col2:
        scraper_type = st.selectbox(
            "🔧 Select Scraper",
            ["Basic Scraper", "FireCrawl Scraper", "Jina Reader", "ScrapeGraphAI"]
        )
    
    # Scraper-specific inputs and processing
    try:
        if scraper_type == "Basic Scraper":
            article_selector = st.text_input("Enter article selector (optional)", "article-title")
            if st.button("🚀 Start Scraping"):
                results = run_basic_scraper(url, article_selector)
                display_results(results, scraper_type)
        
        elif scraper_type == "FireCrawl Scraper":
            if st.button("🚀 Start Scraping") and validate_api_key('firecrawl'):
                results = asyncio.run(run_firecrawl(url, st.session_state.api_keys['firecrawl']))
                display_results(results, scraper_type)
        
        elif scraper_type == "Jina Reader":
            action = st.selectbox("Select Action", ["Read URL", "Summarize", "Extract Images"])
            max_length = None
            if action == "Summarize":
                max_length = st.slider("Summary Length", 100, 500, 200)
            
            if st.button("🚀 Start Processing") and validate_api_key('jina'):
                results = run_jina_reader(
                    url, 
                    st.session_state.api_keys['jina'],
                    action,
                    max_length
                )
                display_results(results, scraper_type)
        
        elif scraper_type == "ScrapeGraphAI":
            graph_type = st.selectbox(
                "Select Graph Type",
                ["SMART_SCRAPER", "SEARCH", "OMNI_SCRAPER"]
            )
            prompt = st.text_area("Enter Prompt", "Extract product information")
            
            if st.button("🚀 Start Processing") and validate_api_key('openai'):
                results = run_scrapegraph(
                    url,
                    st.session_state.api_keys['openai'],
                    graph_type,
                    prompt
                )
                display_results(results, scraper_type)
    
    except ValueError as e:
        st.error(f"❌ Configuration Error: {str(e)}")
    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
        st.exception(e)

if __name__ == "__main__":
    main()
