# CSS Feature Analysis Project

Этот проект предназначен для сбора, анализа и визуализации использования современных CSS-функций на различных веб-сайтах.

## Структура проекта

```
css_analysis_project/
│
├── config.json                       # Конфигурационный файл
├── main.py                           # Основной скрипт для запуска проекта
├── data/
│   ├── domains.json                  # Список доменов для анализа
│   ├── domains-slim.json             # Сжатый список доменов для быстрой проверки работоспособности
│   ├── results.json                  # Результаты сбора CSS-стилей
│   └── css_features_statistics.json  # Статистика использования CSS-функций
│
├── modules/
│   ├── __init__.py
│   ├── css_fetcher.py                # Модуль для сбора CSS-стилей
│   ├── css_analyzer.py               # Модуль для анализа CSS-функций
│   └── visualizer.py                 # Модуль для визуализации данных
│
└── README.md                         # Документация проекта
```

## Конфигурация

Все параметры проекта задаются в файле `config.json`:

```json
{
    "domains_file": "data/domains.json",
    "results_file": "data/results.json",
    "statistics_file": "data/css_features_statistics.json",
    "css_patterns": {
        "attr()": "attr\\(",
        "@container": "@container",
        ":is()": ":is\\(",
        ":where()": ":where\\(",
        ":has()": ":has\\("
    },
    "top_features_to_display": 25
}
```

- **domains_file**: Путь к файлу с доменами для анализа.
- **results_file**: Файл для хранения собранных CSS-стилей.
- **statistics_file**: Файл для хранения статистики CSS-функций.
- **css_patterns**: CSS-функции, которые будут анализироваться.
- **top_features_to_display**: Количество наиболее часто используемых функций для отображения на графике.
