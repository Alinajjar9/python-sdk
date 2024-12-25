import requests
headers = {
    "X-Api-Key": "api key from the web site"
}

response = requests.get("https://api.pokemontcg.io/v2/cards", headers=headers)

if response.status_code == 200:
    data = response.json()

else:
    print(f"Error: {response.status_code} - {response.text}")