from exchange_rates import get_exchange_rates

def convert_currency(amount, from_currency, to_currency):
    # Get exchange rates with from_currency as base
    rates = get_exchange_rates(base_currency=from_currency.upper())
    if rates is None:
        return None
    rate = rates.get(to_currency.upper())
    if rate is None:
        print(f"Conversion rate for {to_currency} not found.")
        return None
    converted_amount = amount * rate
    return converted_amount

if __name__ == "__main__":
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount entered.")
        exit(1)
    from_curr = input("From currency (e.g., USD): ").upper()
    to_curr = input("To currency (e.g., EUR): ").upper()

    result = convert_currency(amount, from_curr, to_curr)
    if result is not None:
        print(f"{amount} {from_curr} is equivalent to {result:.2f} {to_curr}")