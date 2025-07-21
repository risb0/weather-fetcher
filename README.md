# ☁️ Weather Fetcher CLI

A simple Python CLI tool to fetch real-time weather data using the [OpenWeatherMap API](https://openweathermap.org/api).

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/yourusername/weather-fetcher.git
cd weather-fetcher

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add your API key to a .env file
echo "OWM_API_KEY=your_api_key" > .env

# Run the CLI
python main.py London
