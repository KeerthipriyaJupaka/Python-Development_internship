import requests

print("===================================")
print("       CURRENCY CONVERTER")
print("===================================")

try:
    # User input
    from_currency = input("Enter base currency (e.g., USD): ").upper()
    to_currency = input("Enter target currency (e.g., INR): ").upper()
    amount = float(input("Enter amount: "))

    # API URL
    url = f"https://open.er-api.com/v6/latest/{from_currency}"

    # Fetch exchange rates
    response = requests.get(url)
    data = response.json()

    # Check API response
    if data["result"] == "success":

        rates = data["rates"]

        # Check target currency exists
        if to_currency in rates:

            exchange_rate = rates[to_currency]
            converted_amount = amount * exchange_rate

            print("\n===================================")
            print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
            print("===================================")

        else:
            print("\n❌ Invalid target currency code.")

    else:
        print("\n❌ Invalid base currency code.")

# Handle invalid number input
except ValueError:
    print("\n❌ Please enter a valid numeric amount.")

# Handle connection errors
except requests.exceptions.RequestException:
    print("\n❌ Network error. Please check your internet connection.")

# General exception
except Exception as e:
    print("\n❌ Error:", e)
