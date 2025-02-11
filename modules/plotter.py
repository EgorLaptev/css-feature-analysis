import json
import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, config):
        self.statistics_file = config['statistics_file']
        self.top_features_to_display = config['top_features_to_display']

    def plot(self):
        with open(self.statistics_file, 'r', encoding='utf-8') as file:
            sorted_rules = json.load(file)

        top_properties = list(sorted_rules.items())[:self.top_features_to_display]

        properties = [item[0] for item in top_properties]
        frequencies = [item[1] for item in top_properties]

        plt.figure(figsize=(10, 6))
        plt.barh(properties, frequencies, color='skyblue')
        plt.xlabel('Frequency', fontsize=12)
        plt.ylabel('CSS Feature', fontsize=12)
        plt.title('Most Used CSS Features', fontsize=14)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
