import requests
import csv

def get_exchange_rates():
    url = "http://api.nbp.pl/api/exchangerates/tables/C?format=json"
    response = requests.get(url)
    data = response.json()
    return data[0]['rates']

def save_to_csv(rates, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['currency', 'code', 'bid', 'ask'])
        for rate in rates:
            writer.writerow([rate['currency'], rate['code'], rate['bid'], rate['ask']])

rates = get_exchange_rates()
save_to_csv(rates, 'exchange_rates.csv')