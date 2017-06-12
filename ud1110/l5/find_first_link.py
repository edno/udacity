import requests
import bs4
from urllib.parse import urljoin

def find_first_link(url):
    # get the HTML from "url", use the requests library
    response = requests.get(url)
    html = response.text
    # feed the HTML into Beautiful Soup
    soup = bs4.BeautifulSoup(html, "html.parser")

    # stores the first link found in the article, if the article contains no
    # links this value will remain None
    article_link = None

    # find the first link in the article
    content_div = soup.find(id="mw-content-text")
    for element in content_div.find_all("p"):
        anchor = element.find("a", recursive=False)
        if anchor:
            article_link = anchor.get('href')
            break

    # return the first link as a string, or return None if there is no link
    if article_link:
        article_link = urljoin('https://en.wikipedia.org/', article_link)
        return article_link
