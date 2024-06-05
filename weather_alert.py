#!/usr/bin/env python3
import requests

def check_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather = data["weather"][0]["description"]
        temperature_celsius = data["main"]["temp"]
        return weather, temperature_celsius
    else:
        print("Failed to fetch weather data.")
        return None, None

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    api_key = "369f6448dfc3601def7afa4ac2a8227b"
    city = "Houston"

    weather, temperature_celsius = check_weather(api_key, city)

    if weather:
        temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
        print(f"Current weather in {city}: {weather.capitalize()}, {temperature_fahrenheit:.2f}°F")
        if "clear" in weather.lower() or "sun" in weather.lower():
            print("The weather is clear and sunny in Houston today.")
        elif "rain" in weather.lower():
            print("There's a chance of rain today in Houston.")
        elif "thunderstorm" in weather.lower():
            print("A thunderstorm is expected today.")
        else:
            print("No severe weather alerts for Houston today.")
    else:
        print("Could not retrieve weather information.")

if __name__ == "__main__":
    main()
