import json
import requests
from bs4 import BeautifulSoup


class CSSFetcher:
    def __init__(self, config):
        self.domains_file = config['domains_file']
        self.results_file = config['results_file']

    def load_domains(self):
        with open(self.domains_file, 'r') as f:
            return json.load(f)['domains']

    def fetch_styles(self, domain):
        try:
            url = f"https://{domain}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            external_styles = [link['href'] for link in soup.find_all('link', rel='stylesheet') if 'href' in link.attrs]
            inline_styles = [style.get_text() for style in soup.find_all('style')]

            return {'domain': domain, 'external_styles': external_styles, 'inline_styles': inline_styles}
        except Exception as e:
            return {'domain': domain, 'error': str(e)}

    def fetch_all(self):
        domains = self.load_domains()
        results = {'results': [self.fetch_styles(domain) for domain in domains]}

        with open(self.results_file, 'w') as f:
            json.dump(results, f, indent=4)
