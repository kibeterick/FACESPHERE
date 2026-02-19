# Weather API Integration Guide

## Overview
AKIRA now includes weather integration with support for real-time weather data from OpenWeatherMap API.

## Features
- ✅ Current weather conditions
- ✅ 5-day weather forecast
- ✅ Human-readable weather summaries
- ✅ Automatic fallback to simulated data
- ✅ Integrated into Interactive Assistant page

## API Endpoints

### 1. Get Current Weather
```
GET /api/weather/current?location=Kigali
```

**Response:**
```json
{
  "location": "Kigali",
  "country": "RW",
  "temperature": 72,
  "feels_like": 74,
  "humidity": 65,
  "description": "Clear Sky",
  "icon": "01d",
  "wind_speed": 8,
  "pressure": 1015,
  "visibility": 10,
  "sunrise": "6:15 AM",
  "sunset": "6:30 PM",
  "source": "OpenWeatherMap API",
  "timestamp": "2026-02-19T18:30:00"
}
```

### 2. Get Weather Forecast
```
GET /api/weather/forecast?location=Kigali&days=5
```

**Response:**
```json
{
  "location": "Kigali",
  "country": "RW",
  "forecast": [
    {
      "date": "Thursday, February 19",
      "temp_high": 78,
      "temp_low": 65,
      "description": "Clear Sky",
      "icon": "01d",
      "humidity": 60,
      "wind_speed": 7
    }
  ],
  "source": "OpenWeatherMap API",
  "timestamp": "2026-02-19T18:30:00"
}
```

### 3. Get Weather Summary
```
GET /api/weather/summary?location=Kigali
```

**Response:**
```json
{
  "summary": "🌤️ Current weather in Kigali: Clear Sky, 72°F. It feels pleasant.",
  "timestamp": "2026-02-19T18:30:00"
}
```

## Setup Instructions

### Step 1: Get API Key
1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Navigate to API Keys section
4. Copy your API key

### Step 2: Add to Environment
Open your `.env` file and add:
```
WEATHER_API_KEY=your_actual_api_key_here
```

### Step 3: Restart Server
```bash
python flask_app.py
```

## Usage in Code

### Python
```python
from weather_service import weather_service

# Get current weather
weather = weather_service.get_current_weather("Kigali")
print(f"Temperature: {weather['temperature']}°F")

# Get forecast
forecast = weather_service.get_forecast("Kigali", 5)
for day in forecast['forecast']:
    print(f"{day['date']}: {day['temp_high']}°F")

# Get summary
summary = weather_service.get_weather_summary("Kigali")
print(summary)
```

### JavaScript (Frontend)
```javascript
// Get current weather
fetch('/api/weather/current?location=Kigali')
  .then(response => response.json())
  .then(data => {
    console.log(`Temperature: ${data.temperature}°F`);
    console.log(`Condition: ${data.description}`);
  });

// Get weather summary
fetch('/api/weather/summary?location=Kigali')
  .then(response => response.json())
  .then(data => {
    console.log(data.summary);
  });
```

## Fallback Mode
If no API key is provided, the system automatically uses simulated weather data:
- Realistic temperature ranges
- Various weather conditions
- Random but consistent data
- Clear indication that data is simulated

## Display Locations

### Interactive Assistant Page
Weather is displayed in the System Status section:
- Shows current conditions
- Updates when you click "Refresh Status"
- Includes temperature and description

### Future Enhancements
- Weather-based music recommendations
- Weather alerts and warnings
- Integration with smart home (adjust thermostat based on weather)
- Weather-based activity suggestions

## Supported Locations
- Any city name (e.g., "Kigali", "New York", "London")
- City with country code (e.g., "Kigali,RW")
- Coordinates (lat,lon format)

## API Limits (Free Tier)
- 60 calls per minute
- 1,000,000 calls per month
- Current weather data
- 5-day forecast

## Troubleshooting

### Weather not loading?
1. Check if WEATHER_API_KEY is set in .env
2. Verify API key is valid
3. Check internet connection
4. Look for error messages in console

### Getting simulated data?
- This means no API key is configured
- Add WEATHER_API_KEY to .env file
- Restart the Flask server

### API key not working?
- Verify key is correct (no extra spaces)
- Check if key is activated (may take a few minutes)
- Ensure you haven't exceeded API limits

## Example Output

### With API Key:
```
🌤️ Current weather in Kigali: Clear Sky, 72°F. It feels pleasant.
Source: OpenWeatherMap API
```

### Without API Key:
```
🌤️ Current weather in Kigali: Partly Cloudy, 75°F. It feels pleasant.
Source: Simulated (Add WEATHER_API_KEY for real data)
```

## Files Modified
- `weather_service.py` - Weather service module
- `flask_app.py` - Added weather API endpoints
- `templates/interactive.html` - Added weather display
- `.env.example` - Added WEATHER_API_KEY
- `requirements.txt` - Already includes requests library

## Next Steps
1. Get your OpenWeatherMap API key
2. Add it to your .env file
3. Restart the server
4. Visit http://localhost:5000/interactive
5. Click "Refresh Status" to see weather

Enjoy real-time weather in your AKIRA system! 🌤️
