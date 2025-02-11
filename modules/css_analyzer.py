import json
import re
from collections import Counter


class CSSAnalyzer:
    def __init__(self, config):
        self.results_file = config['results_file']
        self.statistics_file = config['statistics_file']
        self.patterns = config['css_patterns']

    def analyze_css_features(self, styles):
        feature_counter = Counter()
        for style in styles:
            clean_style = style.split('/*')[0].strip()
            for feature, pattern in self.patterns.items():
                matches = re.findall(pattern, clean_style)
                if matches:
                    feature_counter[feature] += len(matches)
        return feature_counter

    def analyze_all(self):
        with open(self.results_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        all_features = Counter()
        for entry in data['results']:
            if 'inline_styles' in entry:
                all_features.update(self.analyze_css_features(entry['inline_styles']))

        sorted_features = dict(sorted(all_features.items(), key=lambda item: item[1], reverse=True))

        with open(self.statistics_file, 'w', encoding='utf-8') as outfile:
            json.dump(sorted_features, outfile, ensure_ascii=False, indent=4)

        print(f"CSS feature statistics saved to {self.statistics_file}")
