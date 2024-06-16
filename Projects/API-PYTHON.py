import requests

def get_weather(city):
    api_key = '646824f2b7b86caffec1d0b16ea77f79'  # Replace this with your valid API key
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    try:
        response = requests.get(base_url)
        data = response.json()
        if 'main' in data and 'temp' in data['main'] and 'weather' in data and len(data['weather']) > 0:
            temperature = data['main']['temp']
            weather_desc = data['weather'][0]['description']
            return f"The current temperature in {city} is {temperature}°C with {weather_desc}."
        else:
            print("Incomplete or unexpected data received:")
            print(data)
            return f"Error fetching weather information for {city}: Incomplete or unexpected data received"
    except requests.exceptions.RequestException as e:
        print(e)
        return f"Error fetching weather information for {city}: {e}"
    except Exception as e:
        print(e)
        return f"Error fetching weather information for {city}: {e}"

# Test the function
print(get_weather("Delhi"))