from bs4 import BeautifulSoup
import requests


def find_quotes():
    url = "https://quotes.toscrape.com/page/1/"
    while True:
        print(url)
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')

        quotes_divs = soup.find_all("div", class_="quote")

        for quote_div in quotes_divs:
            phrase = quote_div.find('span', 'text').text
            author = quote_div.find('small', 'author').text
            tags = quote_div.find_all('a', 'tag')

            print(dict({
                "Phrase": phrase,
                "Author": author,
                "Tags": [tag.text for tag in tags]
            }))

        try:
            url = f"https://quotes.toscrape.com{soup.find('li', 'next').a['href']}"

        except Exception:
            print("Última página")
            break


if __name__ == "__main__":
    find_quotes()