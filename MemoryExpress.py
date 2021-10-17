import requests
from bs4 import BeautifulSoup

def formatHyperlink(raw):
    raw = str(raw)

    return 'https://www.memoryexpress.com' + raw


def formatPrice(raw):
    raw = str(raw)

    raw = raw.replace('<span>', '')
    raw = raw.replace('</span>', '')
    return raw.strip()


def getDataME(userSearch):
    response = requests.get('https://www.memoryexpress.com/Search/Products?Search=' + userSearch + '&Sort=Price')
    soup = BeautifulSoup(response.content, 'html.parser')
    results = {}

    items = soup.findAll('div', attrs={'class': 'c-shca-icon-item'})

    count = 1
    for i in items:
        price = i.find_next('div', attrs={'class': 'c-shca-icon-item__summary-list'}).find_next('span')
        hyperlink = i.select_one('.c-shca-icon-item__body-name a')['href']

        price = formatPrice(price)
        hyperlink = formatHyperlink(hyperlink)

        results['#' + str(count)] = [price, hyperlink]
        count += 1

    return results

