from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com/page/1/"
source = requests.get(url).text
soup = BeautifulSoup(source, "html.parser")

def find_quotes():
    quotes_div = soup.find_all("div", class_="quote")
    for quote_div in quotes_div:
        phrase = quote_div.find("span", class_="text").text
        author = quote_div.find("small", class_="author").text
        tags = quote_div.find_all('a', 'tag')
        

        print({"Text": phrase,
        "Author": author,
        "Tags": [tag.text for tag in tags]})

if __name__ == "__main__":
    find_quotes()