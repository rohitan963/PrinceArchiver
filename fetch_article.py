import requests
from bs4 import BeautifulSoup

def fetch_article(url):
    """
    Fetches an article from the given URL and extracts the title and content.
    """
    # Define headers to mimic a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.107 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error fetching page:", response.status_code)
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Example extraction: Adjust selectors based on actual page structure
    title_tag = soup.find('h1')
    title = title_tag.get_text(strip=True) if title_tag else "No title found"
    
    content_div = soup.find('div', class_='article-content')
    content = content_div.get_text(separator='\n', strip=True) if content_div else "No content found"

    return {
        'title': title,
        'content': content
    }

if __name__ == '__main__':
    url = input("Enter the article URL please: ")
    article = fetch_article(url)
    if article:
        print("Title:", article['title'])
        print("Content preview:", article['content'][:200])