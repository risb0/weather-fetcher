#!/bin/bash

# Simple wrapper to run the weather-fetcher CLI

CITY="$1"

if [ -z "$CITY" ]; then
  echo "❌ Error: You must provide a city name."
  echo "Usage: ./run_weather.sh <city>"
  exit 1
fi

if [ ! -f .env ]; then
  echo "❌ Error: .env file not found. Please create it and add your API key."
  exit 1
fi

# Optional: activate virtualenv if present
if [ -d "venv" ]; then
  source venv/bin/activate
fi

# Run the Python script
python main.py "$CITY"
