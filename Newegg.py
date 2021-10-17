import requests
from bs4 import BeautifulSoup

def formatPrice(price):
    price = str(price)

    price = price.replace('<strong>', '')
    price = price.replace('</strong>', '')
    
    return '$' + price


def getDataNewegg(search):
    response = requests.get('https://www.newegg.ca/p/pl?d=' + search + '&Order=1')
    soup = BeautifulSoup(response.content, 'html.parser')
    results = {}

    items = soup.findAll('div', attrs={'class': 'item-cell'})

    count = 1
    for i in items:
        try:
            price = i.find_next('ul', attrs={'class': 'price'}).find_next('strong')
            hyperlink = i.select_one('.item-container a')['href']

            results['#' + str(count)] = [formatPrice(price), hyperlink]
            count += 1
        except:
            pass

    return results
