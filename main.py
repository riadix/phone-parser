import requests
import re
from bs4 import BeautifulSoup

website = input('> Please enter the web page you would like to scan: \n')

response = requests.get(website)
html_content = response.text 

soup = BeautifulSoup(html_content, 'html.parser')

all_numbers = []

divs = soup.find_all('div')
spans = soup.find_all('span')
elements = divs + spans
for elem in elements:
    elem_text = elem.get_text()
    numbers = [
        m.group()
        for m in re.finditer(r'\D((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?(\d[\- ]?){7}\D', elem_text)
    ]
    if numbers != []:
        for num in numbers:
            num = num[1:-1]
            if num not in all_numbers:
                all_numbers.append(num)

chars_to_remove = [' ', '-', '(', ')']
ready_numbers = []

# turn numbers into 8KKKNNNNNNN format
for num in all_numbers:
    for ch in chars_to_remove:
        num = num.replace(ch, '')
    if len(num) == 7:
        num = '8916' + num
    elif len(num) == 10:
        num = '8' + num
    elif len(num) == 12:
        num = '8' + num[2:]
    if len(num) == 11:
        ready_numbers.append(num)

print(ready_numbers)
