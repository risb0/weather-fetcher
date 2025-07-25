---

## 🐳 Run with Docker

```bash
# Build the image
docker build -t weather-fetcher .

# Run with a city and your API key
docker run --rm --env OWM_API_KEY=your_api_key weather-fetcher "Berlin"
