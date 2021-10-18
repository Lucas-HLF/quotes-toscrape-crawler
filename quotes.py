from bs4 import BeautifulSoup
import json
import requests

def page_navegation():
    url = "https://quotes.toscrape.com/page/1/"
    list_quotes = []   
    while True:
        print(f"Página {url[-3::].replace('/', '')}")
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')
        list_quotes.append(find_quotes(soup, list_quotes))
        try:
            url = f"https://quotes.toscrape.com{soup.find('li', 'next').a['href']}"

        except Exception:
            print(f"Última página, Página {url[-3::].replace('/', '')}")
            break

    with open("quote.json", "w", encoding="utf-8") as json_file:
        list_quotes = [i for i in list_quotes if i != None]
        json.dump(list_quotes, json_file)


def format_phrase(phrase):
    new_phrase = phrase.replace('“', "")
    return new_phrase.replace('”', "")


def find_quotes(soup, list_quotes):
    quotes_divs = soup.find_all("div", class_="quote")
    for quote_div in quotes_divs:
        phrase = quote_div.find('span', 'text').text
        author = quote_div.find('small', 'author').text
        tags = quote_div.find_all('a', 'tag')
        
        list_quotes.append(dict({
                "Phrase": format_phrase(phrase),
                "Author": author,
                "Tags": [tag.text for tag in tags]
                }))


if __name__ == "__main__":
    page_navegation()