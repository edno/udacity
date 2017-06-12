import requests
import bs4
from urllib.parse import urljoin
from time import sleep

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophical"

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
    if content_div:
        for element in content_div.find_all("p"):
            anchor = element.find("a", recursive=False)
            if anchor:
                article_link = anchor.get('href')
                break

    # return the first link as a string, or return None if there is no link
    if article_link:
        article_link = urljoin('https://en.wikipedia.org/', article_link)
        return article_link

def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print('Page found')
        return False
    elif len(search_history) > max_steps:
        print('Search is taking too much time')
        return False
    elif search_history[-1] in search_history[:-1]:
        print('Search falls into a cycle')
    else:
        return True

article_chain = [start_url]
while continue_crawl(article_chain, target_url):
    print(article_chain[-1])
    # download html of last article in article_chain
    # find the first link in that html
    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print('Search reaches an article without link')
        break

    # add the first link to article chain
    article_chain.append(first_link)
    # delay for about two seconds
    sleep(2)
