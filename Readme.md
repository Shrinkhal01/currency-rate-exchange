# Currency Rate Exchange

This project provides a simple command-line tool to convert currency amounts using the latest exchange rates from the Frankfurter API.

## Files

- `main.py`: Contains the main script to convert currency amounts.
- `exchange_rates.py`: Contains the function to fetch the latest exchange rates.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Shrinkhal01/currency-rate-exchange.git
    cd currency-rate-exchange
    ```

2. Install the required Python packages:
    ```sh
    pip install requests
    ```

## Usage

Run the main script:
```sh
python main.py
```

## Example

```
Enter the amount: 100
From currency (e.g., USD): USD
To currency (e.g., EUR): EUR
100.0 USD is equivalent to 85.00 EUR
```

## License

This project is licensed under the MIT License.