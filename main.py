import argparse

def get_weather(city):
    # Placeholder for actual weather logic
    print(f"\nWeather for {city}")
    print("-" * 30)
    print("Temperature: 22°C")
    print("Condition: Sunny ☀️")
    print("Humidity: 60%")
    print("Wind: 10 km/h")

def main():
    parser = argparse.ArgumentParser(description="Fetch current weather for a city")
    parser.add_argument("city", type=str, help="City name (e.g., London)")
    args = parser.parse_args()

    get_weather(args.city)

if __name__ == "__main__":
    main()
