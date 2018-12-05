# import libraries
import urllib.request
from bs4 import BeautifulSoup

# specify the url
quote_page = 'http://www.meteovillaverde.es'

# query the website and return the html to the variablb ‘page’
page = urllib.request.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

var1 = 0
for sub_heading in soup.find_all('td'):
    if sub_heading.text == ' Temperatura:':
        var1 = 1
    else:
        if var1 == 1:
            Temperatura = sub_heading.text
            break

# prueba joder
print(Temperatura)
