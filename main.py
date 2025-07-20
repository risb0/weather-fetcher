import argparse
import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("OWM_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if response.status_code != 200:
            print(f"Error: {data.get('message', 'Unknown error')}")
            return

        print(f"\nWeather for {city}")
        print("-" * 30)
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Condition: {data['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind: {data['wind']['speed']} km/h")

    except Exception as e:
        print(f"Request failed: {e}")

def main():
    parser = argparse.ArgumentParser(description="Fetch current weather for a city")
    parser.add_argument("city", type=str, help="City name (e.g., London)")
    args = parser.parse_args()
    get_weather(args.city)

if __name__ == "__main__":
    main()
