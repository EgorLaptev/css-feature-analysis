import json

import requests
from bs4 import BeautifulSoup

# Загружаем список доменов из таблицы
file_path = 'data/domains.json'

with open(file_path, 'r') as f:
    domains = json.load(f)['domains']


# Функция для извлечения CSS с главной страницы сайта
def fetch_styles(domain):
    try:
        url = f"https://{domain}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Сбор внешних таблиц стилей
        external_styles = [link['href'] for link in soup.find_all('link', rel='stylesheet') if 'href' in link.attrs]

        # Сбор встроенных стилей
        inline_styles = [style.get_text() for style in soup.find_all('style')]

        return {
            'domain': domain,
            'external_styles': external_styles,
            'inline_styles': inline_styles
        }
    except Exception as e:
        return {
            'domain': domain,
            'error': str(e)
        }


data = {
    'results': []
}

for domain in domains:
    data['results'].append(fetch_styles(domain))

with open('data/results.json', 'w') as f:
    json.dump(data, f, indent=4)
