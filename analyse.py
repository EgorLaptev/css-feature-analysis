import json
from collections import Counter
import re

# Загружаем данные из JSON-файла
file_path = 'data/results.json'
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Функция для извлечения CSS-правил из строки стилей
def extract_css_rules(styles):
    rules = []
    for style in styles:
        # Убираем комментарии
        clean_style = style.split('/*')[0].strip()
        # Ищем свойства CSS через регулярные выражения
        raw_rules = [line.split(':')[0].strip() for line in clean_style.split(';') if ':' in line]
        # Удаляем браузерные префиксы (-ms-, -moz-, -webkit-, -o- и т.п.)
        normalized_rules = [re.sub(r'^-[a-z]+-', '', rule) for rule in raw_rules]
        rules.extend(normalized_rules)
    return rules

# Сбор всех CSS-правил
all_rules = []
for entry in data['results']:
    if 'inline_styles' in entry:
        all_rules.extend(extract_css_rules(entry['inline_styles']))

# Подсчет частоты каждого CSS-правила
rules_counter = Counter(all_rules)

# Сортировка свойств по возрастанию частоты использования
sorted_rules = dict(sorted(rules_counter.items(), key=lambda item: item[1], reverse=True))

# Сохраняем результаты в JSON
output_file = 'data/css_statistics.json'
with open(output_file, 'w', encoding='utf-8') as outfile:
    json.dump(sorted_rules, outfile, ensure_ascii=False, indent=4)

print(f"Статистика CSS сохранена в файл: {output_file}")
