import requests



# '29da32489aa26561114e4ecd78af19700f50028c'

headers = {
    'Authorization': 'Bearer 29da32489aa26561114e4ecd78af19700f50028c'
}

long_url = input()

payload = {
    'long_url': long_url,
}

api_url = 'https://api-ssl.bitly.com/v4/bitlinks'

response = requests.post(api_url, headers=headers, json=payload)
response.raise_for_status()

print(response.json()['link'])
