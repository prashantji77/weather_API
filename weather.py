import urllib.request  
import json
import ssl

class Weather:
    def __init__(self, city_name):
        self.city_name = city_name

    def weatherapi(self):
        try:
            context = ssl._create_unverified_context()
            with urllib.request.urlopen(f"https://api.tomorrow.io/v4/weather/realtime?location={self.city_name}&apikey=juy8CymL7j4xmcnzbnLX4LU6qLVqbs4j", context=context) as webUrl:
                data = json.loads(webUrl.read().decode())
                return data
        except Exception as e:
            return {"error": str(e)}

city_name = input("Enter your city:")
weather = Weather(city_name)
weather_data = weather.weatherapi()

if 'error' in weather_data:
    print(f"Error: {weather_data['error']}")
else:
    print("Weather Data:")
    print(f"City: {weather_data['location']['name']}")
    print(f"Latitude: {weather_data['location']['lat']}")
    print(f"Longitude: {weather_data['location']['lon']}")
    print(f"Time: {weather_data['data']['time']}")
    print(f"Temperature: {weather_data['data']['values']['temperature']} °C")
    print(f"Humidity: {weather_data['data']['values']['humidity']}%")
    print(f"Wind Speed: {weather_data['data']['values']['windSpeed']} m/s")
    print(f"Cloud Cover: {weather_data['data']['values']['cloudCover']}%")