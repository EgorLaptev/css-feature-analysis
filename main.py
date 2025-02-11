import json
from modules.css_fetcher import CSSFetcher
from modules.css_analyzer import CSSAnalyzer
from modules.plotter import Plotter


def main():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    fetcher = CSSFetcher(config)
    fetcher.fetch_all()

    analyzer = CSSAnalyzer(config)
    analyzer.analyze_all()

    plotter = Plotter(config)
    plotter.plot()


if __name__ == "__main__":
    main()
