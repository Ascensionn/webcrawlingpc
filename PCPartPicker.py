import requests
from bs4 import BeautifulSoup

def formatPrice(price):
    price = str(price)

    index = price.index('>') + 1
    price = price[index : len(price)]
    price = price.replace('</a>', '')
    
    return price


def formatHyperlink(hyperlink):
    hyperlink = str(hyperlink)

    return 'https://pcpartpicker.com' + hyperlink


def getDataPCPartPicker(search):
    response = requests.get('https://pcpartpicker.com/search/?q=' + search)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = {}

    items = soup.findAll('ul', attrs={'class': 'list-unstyled'})

    count = 1
    for i in items:
        try:
            price = i.find_next('a', attrs={'class': 'product__link product__link--price'})
            hyperlink = i.select_one('.search_results--link a')['href']

            results['#' + str(count)] = [formatPrice(price), formatHyperlink(hyperlink)]
            count += 1
        except:
            pass

    return results
