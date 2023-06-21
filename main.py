import os
from dotenv import load_dotenv
import requests
import argparse
from urllib.parse import urlparse


def shorten_link(token, link):
    url = "https://api-ssl.bitly.com/v4/shorten"
    params = {"long_url": link}
    headers = {"Authorization": "Bearer {}".format(token)}
    response = requests.post(url, headers=headers, json=params)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(token, bitlink):
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    params = {"units": "-1", "unit": "month"}
    headers = {"Authorization": "Bearer {}".format(token)}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, bitlink):
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}"
    headers = {"Authorization": "Bearer {}".format(token)}
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description='Данный проект позволит сокращать ссылки.')
    parser.add_argument('--url', help='Введите ссылку')
    args = parser.parse_args()
    token = os.environ['BITLY_TOKEN']
    parsed_url = urlparse(args.url)
    parsed_url = f"{parsed_url.netloc}{parsed_url.path}"
    try:
        if is_bitlink(token, parsed_url):
            print(count_clicks(token, parsed_url))
        else:
            print(shorten_link(token, args.url))
    except requests.exceptions.HTTPError:
        print("Проверьте ссылку которую вы ввели.")


if __name__ == '__main__':
    main()
