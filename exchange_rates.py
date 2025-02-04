import requests

def get_exchange_rates(base_currency="USD"):
    url = f"https://api.frankfurter.app/latest?base={base_currency}"  # Using frankfurter.app for testing
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        data = response.json()
        return data.get("rates")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None