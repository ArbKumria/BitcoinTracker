import requests
import json
import time

def get_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    response = requests.get(url) 

    data = json.loads(response.text)

    return (data["bpi"]["USD"]["rate"])

def main():
    
    print("Welcome to Bitcoin Price Tracker")
   
    while True:
        try:
            bitcoin_price = get_bitcoin_price()
            print(f"Current Bitcoin Price: ${bitcoin_price}")
       
       
        except Exception as e:
            print(f"Error fetching Bitcoin price: {e}")

        # Fetch price every 10 seconds (adjust as needed)
            
        time.sleep(10)
       
       
if __name__ == "__main__":
    main()
