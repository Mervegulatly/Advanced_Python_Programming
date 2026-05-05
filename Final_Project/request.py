import requests
import re

url = "https://api.exchangerate-api.com/v4/latest/USD"
response=requests.get(url=url)

print(response.status_code)

data = response.json()

rates = data["rates"] # Extracting rates data from JSON

secilen_kurlar = {}

for key, value in rates.items():
    if key in ["USD", "EUR", "GBP"]:
        secilen_kurlar[key] = value

print("secilen kurlar:",secilen_kurlar)

for key, value in rates.items():  # We should directly work on the value
    value_str = str(value)
    temiz = re.sub(r"[^\d.]", "", value_str)
    print(key, temiz)