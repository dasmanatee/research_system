"""
Article Downloader
Downloads raw article content from URLs without LLM summarization.
Saves full HTML and extracted text to the raw_information folder.
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import re
import json

# Configuration
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Article URLs to download
URLS = [
    "https://www.constructiondive.com/news/data-center-construction-rolls-into-2026/808636/",
    "https://www.datacenterknowledge.com/data-center-construction/new-data-center-developments-december-2025",
    "https://www.bisnow.com/national/news/data-center-development/whats-next-for-data-center-development-industry-leaders-make-2026-predictions-132606",
    "https://www.datacenterknowledge.com/data-center-construction/2025-s-biggest-data-center-construction-stories-a-year-in-review",
    "https://www.constructiondive.com/news/data-center-projects-construction-2025/738160/",
    "https://www.networkenvironments.com/weekly-digest-u-s-data%E2%80%91center-construction-news-dec-30-jan-6-2026/",
    "https://www.blackridgeresearch.com/blog/upcoming-largest-data-center-projects-in-united-states-usa",
]

def sanitize_filename(url):
    """Create a safe filename from URL."""
    # Extract domain and path
    clean = url.replace("https://", "").replace("http://", "")
    clean = re.sub(r'[^\w\-]', '_', clean)
    clean = re.sub(r'_+', '_', clean)[:100]
    return clean

def extract_article_text(soup):
    """Extract main article text from BeautifulSoup object."""
    # Remove script, style, nav, header, footer elements
    for tag in soup(['script', 'style', 'nav', 'header', 'footer', 'aside', 'iframe', 'noscript']):
        tag.decompose()

    # Try common article containers
    article = None
    for selector in ['article', '[role="main"]', '.article-body', '.post-content',
                     '.entry-content', '.article-content', '.story-body', 'main']:
        article = soup.select_one(selector)
        if article:
            break

    if not article:
        article = soup.find('body') or soup

    # Get text with some structure preserved
    text_parts = []
    for elem in article.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'li', 'blockquote']):
        text = elem.get_text(strip=True)
        if text:
            if elem.name.startswith('h'):
                text_parts.append(f"\n{'#' * int(elem.name[1])} {text}\n")
            elif elem.name == 'li':
                text_parts.append(f"- {text}")
            elif elem.name == 'blockquote':
                text_parts.append(f"> {text}")
            else:
                text_parts.append(text)

    return '\n\n'.join(text_parts)

def download_article(url):
    """Download and save article content."""
    print(f"\nDownloading: {url}")

    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Get title
        title = soup.find('title')
        title_text = title.get_text(strip=True) if title else "Untitled"

        # Extract article text
        article_text = extract_article_text(soup)

        # Create filename
        filename = sanitize_filename(url)

        # Save raw HTML
        html_path = os.path.join(OUTPUT_DIR, f"{filename}.html")
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(response.text)

        # Save extracted text as markdown
        md_path = os.path.join(OUTPUT_DIR, f"{filename}.md")
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(f"# {title_text}\n\n")
            f.write(f"**Source URL**: {url}\n")
            f.write(f"**Downloaded**: {datetime.now().isoformat()}\n\n")
            f.write("---\n\n")
            f.write(article_text)

        print(f"  [OK] Saved: {filename}.html and {filename}.md")
        return {"url": url, "status": "SUCCESS", "files": [html_path, md_path]}

    except requests.exceptions.RequestException as e:
        print(f"  [FAIL] {e}")
        return {"url": url, "status": "FAILED", "error": str(e)}

def main():
    print("=" * 60)
    print("Article Downloader")
    print(f"Downloading {len(URLS)} articles...")
    print("=" * 60)

    results = []
    for url in URLS:
        result = download_article(url)
        results.append(result)

    # Summary
    print("\n" + "=" * 60)
    print("DOWNLOAD SUMMARY")
    print("=" * 60)

    success = sum(1 for r in results if r['status'] == 'SUCCESS')
    failed = sum(1 for r in results if r['status'] == 'FAILED')

    print(f"Successful: {success}")
    print(f"Failed: {failed}")

    if failed > 0:
        print("\nFailed URLs:")
        for r in results:
            if r['status'] == 'FAILED':
                print(f"  - {r['url']}: {r['error']}")

    # Save results log
    log_path = os.path.join(OUTPUT_DIR, "download_results.json")
    with open(log_path, 'w') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "results": results
        }, f, indent=2)

    print(f"\nResults saved to: {log_path}")

if __name__ == "__main__":
    main()
