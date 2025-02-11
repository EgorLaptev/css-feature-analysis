import json
import matplotlib.pyplot as plt


input_file = 'data/css_statistics.json'
with open(input_file, 'r', encoding='utf-8') as file:
    sorted_rules = json.load(file)

top_properties = list(sorted_rules.items())[:25]
properties = [item[0] for item in top_properties]
frequencies = [item[1] for item in top_properties]

plt.figure(figsize=(10, 6))
plt.barh(properties, frequencies, color='skyblue')
plt.xlabel('Frequency', fontsize=12)
plt.ylabel('CSS Property', fontsize=12)
plt.title('Most Used CSS Properties', fontsize=14)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()
