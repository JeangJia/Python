from lxml import html
import requests

URL = 'https://www.themoviedb.org/movie/top-rated'


def main():
    with open('20 movie.html', 'w', encoding='utf-8') as f:
        ret = requests.get(URL)
        f.write(ret.text)
        doc = html.fromstring(ret.text)


if __name__ == '__main__':
    main()
