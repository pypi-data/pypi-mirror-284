import requests

def get_coin_data(mint_str):
    url = f"https://frontend-api.pump.fun/coins/{mint_str}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "If-None-Match": 'W/"41b-5sP6oeDs1tG//az0nj9tRYbL22A"',
        "Priority": "u=4"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        return None