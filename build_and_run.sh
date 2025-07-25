#!/bin/bash

# Usage: ./build_and_run.sh <city> <api_key>

CITY="$1"
API_KEY="$2"

if [ -z "$CITY" ] || [ -z "$API_KEY" ]; then
  echo "❌ Usage: ./build_and_run.sh <city> <api_key>"
  exit 1
fi

echo "🔨 Building Docker image..."
docker build -t weather-fetcher .

echo "🚀 Running for city: $CITY"
docker run --rm --env OWM_API_KEY="$API_KEY" weather-fetcher "$CITY"
