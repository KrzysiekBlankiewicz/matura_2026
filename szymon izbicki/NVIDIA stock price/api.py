import requests

symbol = "NVDA"

def get_dane_gieldowe():
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=60min&outputsize=full&apikey=NN72ZY1E0K3QXSBK"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        time_series = data["Time Series (60min)"]

        with open("nvda_data.txt", "w") as f:
            f.write("datetime\thigh\tlow\topen\n")

            for time in sorted(time_series.keys()):
                candle = time_series[time]

                high = candle["2. high"]
                low = candle["3. low"]
                open_price = candle["1. open"]

                f.write(f"{time}\t{high}\t{low}\t{open_price}\n")

        return True
    else:
        print("Failed:", response.status_code)
        return False

get_dane_gieldowe()