
import requests
def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    

    response = requests.get(complete_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_description = data['weather'][0]['description']

        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        wind_speed = wind['speed']


        print(f'city: {city}')  
        print(f'temperature: {temperature}°C')
        print(f'pressure: {pressure} hPa')
        print(f'humidity: {humidity}%')
        print(f'wind speed: {wind_speed} m/s')
        print(f'weather description: {weather_description}')
    else:
        print("City not found.")

def main():
    api_key = 'your_api_key_here'  
    city = input("Enter city name: ")
    get_weather(api_key, city)

if __name__ == "__main__":
    main()