from urllib.parse import urlparse
import requests
import os


api_token = os.getenv("TOKEN")


url = input()


def shorten_link(token, url):
    response = requests.post(
        'https://api-ssl.bitly.com/v4/bitlinks', 
        headers={'Authorization': 'Bearer ' + token},
        json={'long_url': url})
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, url):
    response = requests.get(
        'https://api-ssl.bitly.com/v4/bitlinks/{0}{1}/clicks/summary'
        .format(url.netloc, url.path),
        headers={'Authorization': 'Bearer ' + token},)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(token, url):
    response = requests.get(
        'https://api-ssl.bitly.com/v4/bitlinks/{0}{1}'
        .format(url.netloc, url.path),
        headers={'Authorization': 'Bearer ' + token},)
    return response.ok

parsed_bitlink = urlparse(url)


try:
    if is_bitlink(api_token, parsed_bitlink):
        total_clicks = count_clicks(api_token, parsed_bitlink)
        print(total_clicks)
    else:
        bitlink = shorten_link(api_token, url)
        print(bitlink)
except requests.exceptions.HTTPError:
    exit('Вы ввели неверную ссылку!')
