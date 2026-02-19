"""
Weather Service - Get current weather and forecasts
Supports OpenWeatherMap API with fallback to simulated data
"""
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class WeatherService:
    """Weather service with real API and fallback"""
    
    def __init__(self):
        self.api_key = os.getenv('WEATHER_API_KEY', '')
        self.base_url = "http://api.openweathermap.org/data/2.5"
        self.default_location = "Kigali"  # Default location
        
        if self.api_key:
            print("✅ Weather API key found")
        else:
            print("⚠️  No WEATHER_API_KEY found. Using simulated weather data.")
    
    def get_current_weather(self, location=None):
        """Get current weather for a location"""
        location = location or self.default_location
        
        # Try real API if key is available
        if self.api_key:
            try:
                return self._get_real_weather(location)
            except Exception as e:
                print(f"⚠️  Weather API error: {e}")
                return self._get_simulated_weather(location)
        else:
            return self._get_simulated_weather(location)
    
    def _get_real_weather(self, location):
        """Get real weather from OpenWeatherMap API"""
        url = f"{self.base_url}/weather"
        params = {
            'q': location,
            'appid': self.api_key,
            'units': 'imperial'  # Fahrenheit
        }
        
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        return {
            'location': data['name'],
            'country': data['sys']['country'],
            'temperature': round(data['main']['temp']),
            'feels_like': round(data['main']['feels_like']),
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'].title(),
            'icon': data['weather'][0]['icon'],
            'wind_speed': round(data['wind']['speed']),
            'pressure': data['main']['pressure'],
            'visibility': data.get('visibility', 10000) / 1000,  # Convert to km
            'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%I:%M %p'),
            'sunset': datetime.fromtimestamp(data['sys']['sunset']).strftime('%I:%M %p'),
            'source': 'OpenWeatherMap API',
            'timestamp': datetime.now().isoformat()
        }
    
    def _get_simulated_weather(self, location):
        """Get simulated weather data (fallback)"""
        import random
        
        conditions = [
            ('Clear', 'clear sky', '01d'),
            ('Partly Cloudy', 'few clouds', '02d'),
            ('Cloudy', 'scattered clouds', '03d'),
            ('Overcast', 'broken clouds', '04d'),
            ('Light Rain', 'light rain', '10d'),
            ('Sunny', 'clear sky', '01d')
        ]
        
        condition = random.choice(conditions)
        temp = random.randint(65, 85)
        
        return {
            'location': location,
            'country': 'RW',
            'temperature': temp,
            'feels_like': temp + random.randint(-3, 3),
            'humidity': random.randint(40, 70),
            'description': condition[1].title(),
            'icon': condition[2],
            'wind_speed': random.randint(3, 12),
            'pressure': random.randint(1010, 1020),
            'visibility': 10,
            'sunrise': '6:15 AM',
            'sunset': '6:30 PM',
            'source': 'Simulated (Add WEATHER_API_KEY for real data)',
            'timestamp': datetime.now().isoformat()
        }
    
    def get_forecast(self, location=None, days=5):
        """Get weather forecast"""
        location = location or self.default_location
        
        # Try real API if key is available
        if self.api_key:
            try:
                return self._get_real_forecast(location, days)
            except Exception as e:
                print(f"⚠️  Forecast API error: {e}")
                return self._get_simulated_forecast(location, days)
        else:
            return self._get_simulated_forecast(location, days)
    
    def _get_real_forecast(self, location, days):
        """Get real forecast from OpenWeatherMap API"""
        url = f"{self.base_url}/forecast"
        params = {
            'q': location,
            'appid': self.api_key,
            'units': 'imperial',
            'cnt': days * 8  # 8 forecasts per day (3-hour intervals)
        }
        
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        # Group by day
        daily_forecasts = []
        current_day = None
        day_data = []
        
        for item in data['list']:
            date = datetime.fromtimestamp(item['dt']).date()
            
            if date != current_day:
                if day_data:
                    daily_forecasts.append(self._aggregate_day_forecast(day_data))
                current_day = date
                day_data = [item]
            else:
                day_data.append(item)
        
        if day_data:
            daily_forecasts.append(self._aggregate_day_forecast(day_data))
        
        return {
            'location': data['city']['name'],
            'country': data['city']['country'],
            'forecast': daily_forecasts[:days],
            'source': 'OpenWeatherMap API',
            'timestamp': datetime.now().isoformat()
        }
    
    def _aggregate_day_forecast(self, day_data):
        """Aggregate 3-hour forecasts into daily forecast"""
        temps = [item['main']['temp'] for item in day_data]
        descriptions = [item['weather'][0]['description'] for item in day_data]
        
        # Most common description
        description = max(set(descriptions), key=descriptions.count)
        
        return {
            'date': datetime.fromtimestamp(day_data[0]['dt']).strftime('%A, %B %d'),
            'temp_high': round(max(temps)),
            'temp_low': round(min(temps)),
            'description': description.title(),
            'icon': day_data[len(day_data)//2]['weather'][0]['icon'],
            'humidity': day_data[len(day_data)//2]['main']['humidity'],
            'wind_speed': round(day_data[len(day_data)//2]['wind']['speed'])
        }
    
    def _get_simulated_forecast(self, location, days):
        """Get simulated forecast data"""
        import random
        from datetime import timedelta
        
        conditions = [
            ('Clear', 'clear sky', '01d'),
            ('Partly Cloudy', 'few clouds', '02d'),
            ('Cloudy', 'scattered clouds', '03d'),
            ('Light Rain', 'light rain', '10d'),
            ('Sunny', 'clear sky', '01d')
        ]
        
        forecasts = []
        base_temp = random.randint(70, 80)
        
        for i in range(days):
            date = datetime.now() + timedelta(days=i)
            condition = random.choice(conditions)
            temp_variation = random.randint(-5, 5)
            
            forecasts.append({
                'date': date.strftime('%A, %B %d'),
                'temp_high': base_temp + temp_variation + random.randint(0, 5),
                'temp_low': base_temp + temp_variation - random.randint(5, 10),
                'description': condition[1].title(),
                'icon': condition[2],
                'humidity': random.randint(40, 70),
                'wind_speed': random.randint(3, 12)
            })
        
        return {
            'location': location,
            'country': 'RW',
            'forecast': forecasts,
            'source': 'Simulated (Add WEATHER_API_KEY for real data)',
            'timestamp': datetime.now().isoformat()
        }
    
    def get_weather_summary(self, location=None):
        """Get a human-readable weather summary"""
        weather = self.get_current_weather(location)
        
        temp = weather['temperature']
        desc = weather['description']
        
        # Temperature feeling
        if temp < 50:
            feeling = "cold"
        elif temp < 65:
            feeling = "cool"
        elif temp < 75:
            feeling = "pleasant"
        elif temp < 85:
            feeling = "warm"
        else:
            feeling = "hot"
        
        summary = f"🌤️ Current weather in {weather['location']}: {desc}, {temp}°F. It feels {feeling}."
        
        # Add wind info if significant
        if weather['wind_speed'] > 15:
            summary += f" Windy at {weather['wind_speed']} mph."
        
        # Add humidity info if high
        if weather['humidity'] > 70:
            summary += f" Humidity is {weather['humidity']}%."
        
        return summary


# Global instance
weather_service = WeatherService()


if __name__ == '__main__':
    print("="*60)
    print("🌤️  Weather Service - Test")
    print("="*60)
    
    # Test current weather
    print("\n📍 Current Weather:")
    weather = weather_service.get_current_weather("Kigali")
    print(f"   Location: {weather['location']}, {weather['country']}")
    print(f"   Temperature: {weather['temperature']}°F (feels like {weather['feels_like']}°F)")
    print(f"   Condition: {weather['description']}")
    print(f"   Humidity: {weather['humidity']}%")
    print(f"   Wind: {weather['wind_speed']} mph")
    print(f"   Source: {weather['source']}")
    
    # Test summary
    print("\n📝 Weather Summary:")
    summary = weather_service.get_weather_summary("Kigali")
    print(f"   {summary}")
    
    # Test forecast
    print("\n📅 5-Day Forecast:")
    forecast = weather_service.get_forecast("Kigali", 5)
    for day in forecast['forecast']:
        print(f"   {day['date']}: {day['temp_high']}°F/{day['temp_low']}°F - {day['description']}")
    
    print(f"\n   Source: {forecast['source']}")
    print("\n✅ Weather service tested!")
